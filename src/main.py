import yt_dlp
import ffmpeg


##################### Download Youtube Videos to Local Drive ###############################

# YOUTUBE_LINK = "https://youtu.be/rqTl-livoRo"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/65ya2V7Gi74"


# # Specifies the output folder for the yt-dlp video downloads
# yt_options = {
#     'outtmpl':"./data/videos/%(title)s.%(ext)s",
#     'merge_output_format': 'mp4'
# }

# with yt_dlp.YoutubeDL(yt_options) as ydl:
#     #download function below takes a list of urls
#     ydl.download([SHORTER_YOUTUBE_LINK])


##################### Extracting Audio from Downloaded Videos ###############################
video_file = ffmpeg.input("./data/videos/Theater of Politics.mp4")
# video_file.output("./data/audio/audio.mp3", acodec="mp3").run()
video_file.output("./data/audio/audio.wav", acodec="pcm_s16le").run()



