import yt_dlp
import subprocess


##################### Download Youtube Videos to Local Drive ###############################

YOUTUBE_LINK = "https://youtu.be/rqTl-livoRo"
SHORTER_YOUTUBE_LINK = "https://youtu.be/65ya2V7Gi74"


# Specifies the output folder for the yt-dlp video downloads
yt_options = {
    'outtmpl':"./data/videos/%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(yt_options) as ydl:
    #download function below takes a list of urls
    ydl.download([SHORTER_YOUTUBE_LINK])

