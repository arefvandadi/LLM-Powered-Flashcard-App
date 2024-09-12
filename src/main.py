from media_processor import MediaProcessor
from words_saver import words_saver


# SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
SHORTER_YOUTUBE_LINK = "https://youtu.be/Sbo8R-v7s98"

youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
print(words_list)
print(definition_list)
# print(type(words_list))

words_saver(words_list, definition_list)






