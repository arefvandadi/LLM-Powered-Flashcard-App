from media_processor import MediaProcessor
from words_saver import words_saver
from tkinter import * 
import pandas as pd
from canvas import CanvasManager
from buttons import ButtonManager

BACKGROUND_COLOR = "#B1DDC6"
SHOW_ANSWER_BACKGROUND_COLOR = "#00ac00"

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


###################### Import Words Repository ##########################
# words_repo = pd.read_csv("./data/words/words_to_learn.csv")
# print(words_repo.iloc[0,0])
# print(words_repo.iloc[0,1])
# print(words_repo.columns[0])

###################### Main Window #######################
window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

# Main Canvas for showing words and meanings in the App
canvas_manager = CanvasManager()
canvas_manager.create_canvas()

# Main Buttons and their functionality
button_manager = ButtonManager(window, canvas_manager)
button_manager.create_buttons()



window.mainloop()


