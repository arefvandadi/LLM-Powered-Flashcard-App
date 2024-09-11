import yt_dlp
import os

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

    
    def __init__(self, youtube_url: str=None, video_destination_folder: str = "./data/videos/"):
        self.youtube_url = youtube_url
        self.video_destination_folder = video_destination_folder


    def youtube_video_downloader(self):
        """
        Downloads a video from a YouTube url.

        Parameters:
        -----------
        youtube_url : str
            A required string of YouTube video URL to be downloaded.
        
        video_destination_folder : str, optional
            The directory where the downloaded videos will be stored. Defaults to `./data/videos` 
            if no path is provided.

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
                print(info_dict.get("title"))
                print(info_dict.get("original_url"))
        else:
            print("No Youtube URL was provided in MediaProcessor class")



# SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
# youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
# youtube_handler.youtube_video_downloader()