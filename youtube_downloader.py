import yt_dlp
import os


def youtube_video_downloader(link: list, video_destination_folder: str):
    
    # Add a line to check if ./data/videos/ folder is available and if it is not create it.
    if not os.path.isdir(video_destination_folder):
        os.makedirs(video_destination_folder)

    # Specifies the output folder for the yt-dlp video downloads
    yt_options = {
        'outtmpl':video_destination_folder + "%(title)s.%(ext)s",
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(yt_options) as ydl:
        #download function below takes a list of urls
        ydl.download(link)