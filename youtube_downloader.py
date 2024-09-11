import yt_dlp


def youtube_video_downloader(link: list):
    
    # Specifies the output folder for the yt-dlp video downloads
    yt_options = {
        'outtmpl':"./data/videos/%(title)s.%(ext)s",
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(yt_options) as ydl:
        #download function below takes a list of urls
        ydl.download(link)