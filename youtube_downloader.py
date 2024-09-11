import yt_dlp
import os


def youtube_video_downloader(youtube_url: str, video_destination_folder: str = "./data/videos/"):
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
        info_dict = ydl.extract_info(youtube_url, download=True)
        print(info_dict.get("title"))
        print(info_dict.get("original_url"))
        # ydl.download(link_list)


SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"

youtube_video_downloader(SHORTER_YOUTUBE_LINK)