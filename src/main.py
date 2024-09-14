from tkinter import Tk
import pandas as pd
from canvas import CanvasManager
from buttons import ButtonManager
from menu_bar import MenuBarManager
from media_processor import MediaProcessor
from word_repository import WordRepoManager

BACKGROUND_COLOR = "#B1DDC6"

################################ Youtube Link Examples ############################################
# # SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/Sbo8R-v7s98"


###################### Main Window #######################
window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

# Word Repository Manager
word_repo_manager = WordRepoManager(window)

# Create Manu Bar and Handle Importing Words by Using media_processor and words_saver modules
menu_bar_manager = MenuBarManager(window, MediaProcessor, word_repo_manager)
menu_bar_manager.create_menu()


# Main Canvas for showing words and meanings in the App
canvas_manager = CanvasManager(word_repo_manager)
canvas_manager.create_canvas()

# Main Buttons and their functionality
button_manager = ButtonManager(window, canvas_manager, word_repo_manager)
button_manager.create_buttons()


# Changes the closing protocol of the app window. 
# It binds the actions of closing the window with the update_word_repo_csv method in word_repository module. 
window.protocol("WM_DELETE_WINDOW", word_repo_manager.update_word_repo_csv)

window.mainloop()


