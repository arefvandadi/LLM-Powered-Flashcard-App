import yt_dlp
import os
import ffmpeg
from transformers import pipeline
import textwrap
from openai import OpenAI
from dotenv import load_dotenv
from config.app_config import (
    DOWNLOADED_VIDEO_NAME,
    GPT_MODEL,
    OPENAI_API_KEY_ENV_VARIABLE,
)

class MediaProcessor:
    """
    A class to handle various media processing tasks for YouTube videos.

    This class provides methods to perform the following tasks:
        - Download a YouTube video.
        - Extract audio from the downloaded video.
        - Transcribe text from the extracted audio.
        - Extraxt important words from the tanscribed text 

    Attributes:
        youtube_link (str): The URL of the YouTube video to be processed.
        delete_media (bool, optional): Deletes Downloaded/Extracted Video, Audio and Text after Words Repo is updated. Set to False to Keep the Media.
        video_destination_folder (str, optional): The path where the downloaded video is stored.
        audio_destination_folder (str, optional): The path where the extracted audio is stored.
        text_destination_folder (str, optional): The path where the extracted text (transcription) is stored.

    Methods:
        youtube_video_downloader: Downloads the video from YouTube and stores it at the specified path.
        audio_extractor: Extracts audio from the downloaded video and saves it to the specified path.
        transcriber: Transcribes the text from the extracted audio.
        words_finder_gpt: Uses GPT4 to find important words in the trnascription
        extract_words_from_youtube_pipeline: Performs the entire pipeline: downloads video, extracts audio, transcribes the text and creates a python list of words.
    """

    
    def __init__(self, youtube_url: str=None, delete_media: bool=True, video_destination_folder: str = "./data/videos/", audio_destination_folder: str = "./data/audio/", text_destination_folder: str="./data/text/"):
        self.youtube_url = youtube_url
        self.delete_media = delete_media
        self.video_destination_folder = video_destination_folder
        self.audio_destination_folder = audio_destination_folder
        self.text_destination_folder = text_destination_folder
        self.youtube_video_title: str = None
        self.original_youtube_url: str = None
        self.audio_wav_created: bool = False
        self.transcription: str | None = None
        self.gpt_prompt_template: str | None = None
        self.gpt_model: str = GPT_MODEL[0]
        self.word_list: list | None = None
        self.definition_list: list | None = None
        self.gpt_definition_prompt_template: str | None = None



    def youtube_video_downloader(self) -> None:
        """
        Downloads a video from a YouTube url
        Updates "youtube_video_title" and "original_youtube_url" class attributes

        Returns:
        --------
        None
        """
        if self.youtube_url:
            # Add a line to check if ./data/videos/ folder is available and if it is not create it.
            if not os.path.isdir(self.video_destination_folder):
                os.makedirs(self.video_destination_folder)

            # Specifies the output folder for the yt-dlp video downloads
            yt_options = {
                'outtmpl':self.video_destination_folder + DOWNLOADED_VIDEO_NAME + ".%(ext)s",
                'merge_output_format': 'mp4'
            }

            with yt_dlp.YoutubeDL(yt_options) as ydl:
                #download function below takes a list of urls
                info_dict = ydl.extract_info(self.youtube_url, download=True)
                
                # Updates "youtube_video_title" and "original_youtube_url" class attributes 
                self.youtube_video_title = info_dict.get("title")
                self.original_youtube_url = info_dict.get("original_url")
               
        else:
            print("No Youtube URL was provided in MediaProcessor class")


    def audio_extractor(self) -> None:
        """
        Takes the video downloaded by the youtube_video_downloader method and extracts audio as a wav file

        Returns:
        -------------
        None
        """
        # This if statement ensures that the downloader was run and youtube video was downloaded and available
        if self.youtube_video_title and self.original_youtube_url:
            video_file = ffmpeg.input(self.video_destination_folder + DOWNLOADED_VIDEO_NAME + ".mp4")
            video_file.output(self.audio_destination_folder + DOWNLOADED_VIDEO_NAME + "_audio.wav", acodec="pcm_s16le").run()
            self.audio_wav_created = True
        else:
            print("No youtube video is available. Please make sure a video is downloaded first using youtube_video_downloader method")


    def _generate_gpt_prompt_template(self) -> str:
        """
        Creates a prompt for GPT model to extract words

        Returns:
        -------------
        str
            A prompt template that includes the transcription from the video from youtube
        """
        return f"""
    Please investigate the 'context' provided below and categorize the words used in the context into three categories based on their difficulty for an English as Second Language (ESL) Learner:
        - Category A: Advanced
        - Category B: Intermediate
        - Category C: Beginner
    
    Subsequently, create a python list of only the words in the Category A: Advanced. 
    I want only the python list in the output and nothing else. 
    I should be able to use eval() function on the output with no error.
    As an example, the final output should like this (feel free to add as many words in the list as long as they are in Category A: Advanced) with no leading and trailing text: ["subsequent", "conversion", "Dice"]


    <Start of context> 
    {self.transcription}
    <END of context>

    """

    def transcriber(self) -> None:
        """
        Uses openai/whisper-small free LLM from HuggingFace to create transcription from audio. 

        Returns:
        -------------
        None
        """
        if self.audio_wav_created:
            pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
            output = pipe(self.audio_destination_folder + DOWNLOADED_VIDEO_NAME + "_audio.wav")
            transcription_text = output["text"]
            wrapped_transcription = textwrap.fill(transcription_text, width=80)
            self.transcription = wrapped_transcription
            
            # following line updates self.gpt_prompt_template attribute with the updated self.transcription from previous line 
            self.gpt_prompt_template = self._generate_gpt_prompt_template()

            with open(self.text_destination_folder + DOWNLOADED_VIDEO_NAME + "_transcription.txt", "w") as file:
                file.write(self.transcription)
        else:
            print("No audio file is available. Make sure audio_extractor is run before runnig this method")


    def words_finder_gpt(self) -> list[str]:
        """
        Uses GPT4 API to create python list of important words found in the transcription generated by transcriber() method 

        Returns:
        -------------
        list
            A python list of important words
        """
        if not os.getenv(OPENAI_API_KEY_ENV_VARIABLE):
            load_dotenv()
        api_key = os.getenv(OPENAI_API_KEY_ENV_VARIABLE)
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
        model=self.gpt_model,
        messages=[
            {"role": "user", "content": self.gpt_prompt_template}
        ]
        )
        self.word_list = eval(completion.choices[0].message.content)
        # return completion.choices[0].message.content
        return self.word_list
    

    def _generate_gpt_definition_prompt_template(self) -> str:
        """
        Creates a prompt for GPT model to return definition of the words

        Returns:
        -------------
        str
            A prompt template that includes the list of words
        """
        return f"""
    words = {self.word_list}

    Please provide the definitions for the words above. 
    Return a Python list where each element is a clear and concise definition of the corresponding word. 
    The list should only contain the definitions and should be formatted as follows with no leading or trailing text:
    
    [
    'definition of word1',
    'definition of word2',
    'definition of word3',
    ...
    ]

    """

    def definition_finder_gpt(self) -> list[str]:
        """
        Uses GPT4 API to create python list of definitions of the words found in the transcription generated by transcriber() method 

        Returns:
        -------------
        list
            A python list of definitions of the words
        """
        self.gpt_definition_prompt_template = self._generate_gpt_definition_prompt_template()
        if not os.getenv(OPENAI_API_KEY_ENV_VARIABLE):
            load_dotenv()
        api_key = os.getenv(OPENAI_API_KEY_ENV_VARIABLE)
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
        model=self.gpt_model,
        messages=[
            {"role": "user", "content": self.gpt_definition_prompt_template}
        ]
        )
        self.definition_list = eval(completion.choices[0].message.content)
        # return completion.choices[0].message.content
        return self.definition_list


    def media_files_deleter(self):
        if self.delete_media:
            os.remove(self.video_destination_folder + DOWNLOADED_VIDEO_NAME + ".mp4")
            os.remove(self.audio_destination_folder + DOWNLOADED_VIDEO_NAME + "_audio.wav")
            os.remove(self.text_destination_folder + DOWNLOADED_VIDEO_NAME + "_transcription.txt")

    
    def extract_words_from_youtube_pipeline(self) -> tuple[list[str], list[str]]:
        """
        Full Youtube video to a extracted python list of important words pipeline

        Returns:
        -----------
        list:
            A python list of important words
        """
        self.youtube_video_downloader()
        self.audio_extractor()
        self.transcriber()
        list_of_words = self.words_finder_gpt()
        list_of_definitons = self.definition_finder_gpt()
        self.media_files_deleter()
        return list_of_words, list_of_definitons