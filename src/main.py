from media_processor import MediaProcessor
from words_saver import words_saver
from tkinter import * 

BACKGROUND_COLOR = "#B1DDC6"

#######################################################################################

# # SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/Sbo8R-v7s98"

# youtube_handler = MediaProcessor(youtube_url=SHORTER_YOUTUBE_LINK)
# words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
# print(words_list)
# print(definition_list)
# # print(type(words_list))

# words_saver(words_list, definition_list)

#######################################################################################

window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

# Main Canvas for showing words and meanings in the App
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=3)









window.mainloop()


