from tkinter import Tk
import pandas as pd
from canvas import CanvasManager
from buttons import ButtonManager
from menu_bar import MenuBarManager
from media_processor import MediaProcessor
from words_saver import words_saver

BACKGROUND_COLOR = "#B1DDC6"

################################ Youtube Link Examples ############################################
# # SHORTER_YOUTUBE_LINK = "https://youtu.be/yY_kCcQ1r64"
# SHORTER_YOUTUBE_LINK = "https://youtu.be/Sbo8R-v7s98"


###################### Main Window #######################
window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

# Create Manu Bar and Handle Importing Words by Using media_processor and words_saver modules
menu_bar_manager = MenuBarManager(window, MediaProcessor, words_saver)
menu_bar_manager.create_menu()


# Main Canvas for showing words and meanings in the App
canvas_manager = CanvasManager()
canvas_manager.create_canvas()

# Main Buttons and their functionality
button_manager = ButtonManager(window, canvas_manager)
button_manager.create_buttons()



window.mainloop()


