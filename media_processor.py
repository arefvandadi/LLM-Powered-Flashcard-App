import yt_dlp
import os
import ffmpeg
from transformers import pipeline
import textwrap
from openai import OpenAI

class MediaProcessor:
    """
    A class to handle various media processing tasks for YouTube videos.

    This class provides methods to perform the following tasks:
        - Download a YouTube video.
        - Extract audio from the downloaded video.
        - Transcribe text from the extracted audio.

    Attributes:
        youtube_link (str): The URL of the YouTube video to be processed.
        video_path (str, optional): The path where the downloaded video is stored.
        audio_path (str, optional): The path where the extracted audio is stored.
        transcription (str, optional): The transcribed text from the audio.

    Methods:
        download_video(download_path='./data/videos'): Downloads the video from YouTube and stores it at the specified path.
        extract_audio(audio_path='./data/audio'): Extracts audio from the downloaded video and saves it to the specified path.
        transcribe_audio(): Transcribes the text from the extracted audio.
        youtube_to_transcription(): Performs the entire pipeline: downloads video, extracts audio, and transcribes the text.
    """

    
    def __init__(self, youtube_url: str=None, video_destination_folder: str = "./data/videos/", audio_destination_folder = "./data/audio/", text_destination_folder="./data/text/"):
        self.youtube_url = youtube_url
        self.video_destination_folder = video_destination_folder
        self.audio_destination_folder = audio_destination_folder
        self.text_destination_folder = text_destination_folder
        self.youtube_video_title = None
        self.original_youtube_url = None
        self.audio_wav_created = False
        self.transcription = None
        self.gpt_prompt_template = None
        self.gpt_model = "gpt-4o-mini"


    def youtube_video_downloader(self):
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
                'outtmpl':self.video_destination_folder + "%(title)s.%(ext)s",
                'merge_output_format': 'mp4'
            }

            with yt_dlp.YoutubeDL(yt_options) as ydl:
                #download function below takes a list of urls
                info_dict = ydl.extract_info(self.youtube_url, download=True)
                
                # Updates "youtube_video_title" and "original_youtube_url" class attributes 
                self.youtube_video_title = info_dict.get("title")
                self.original_youtube_url = info_dict.get("original_url")
                # print(info_dict.get("title"))
                # print(info_dict.get("original_url"))
        else:
            print("No Youtube URL was provided in MediaProcessor class")


    def audio_extractor(self):
        # This if statement ensures that the downloader was run and youtube video was downloaded and available
        if self.youtube_video_title and self.original_youtube_url:
            video_file = ffmpeg.input(self.video_destination_folder + self.youtube_video_title + ".mp4")
            video_file.output(self.audio_destination_folder + self.youtube_video_title + "_audio.wav", acodec="pcm_s16le").run()
            self.audio_wav_created = True
        else:
            print("No youtube video is available. Please make sure a video is downloaded first using youtube_video_downloader method")


    def _generate_gpt_prompt_template(self):
        return f"Please investigate the following 'context' and create a list of \
            English words in the context provided that \
                is good for an intermediate english as a second language learner, \
                    to practice and improve his/her vocabulaory:\
        \n\ncontext = {self.transcription}\
        \n\nNotice there is no need for explaining the meaning of the word. The response should only include the words\
          in the format of a python list. No explanations before or after the python list.\
        \n\n Also there is no need to output words = [], remove the 'words =' and only output the python list"

    def transcriber(self):
        if self.audio_wav_created:
            pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")
            output = pipe(self.audio_destination_folder + self.youtube_video_title + "_audio.wav")
            transcription_text = output["text"]
            wrapped_transcription = textwrap.fill(transcription_text, width=80)
            self.transcription = wrapped_transcription
            
            # following line updates self.gpt_prompt_template attribute with the updated self.transcription from previous line 
            self.gpt_prompt_template = self._generate_gpt_prompt_template()

            with open(self.text_destination_folder + self.youtube_video_title + "_transcription.txt", "w") as file:
                file.write(self.transcription)
        else:
            print("No audio file is available. Make sure audio_extractor is run before runnig this method")


    def get_gpt_response(self):
        api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
        # model="gpt-4o",
        model=self.gpt_model,
        messages=[
            {"role": "user", "content": self.gpt_prompt_template}
        ]
        )
        return completion.choices[0].message.content


# SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
# youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
# youtube_handler.youtube_video_downloader()
# youtube_handler.audio_extractor()
# youtube_handler.transcriber()
# print(youtube_handler.get_gpt_response())