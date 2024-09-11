from media_processor import MediaProcessor


SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"

youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
words_list = youtube_handler.extract_words_from_youtube()
print(words_list)






