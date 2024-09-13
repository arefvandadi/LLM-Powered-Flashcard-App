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

###################### Youtube Importing Menu #######################
def youtube_import_from_menu():
    """Function to open a new window for YouTube URL input."""
    # Create a new top-level window
    youtube_window = Toplevel(window, padx=20, pady=20)
    youtube_window.title("Import from YouTube")


    # Disable the main window
    # window.attributes('-disabled', True)
    # Make sure the top-level window grabs all events
    # youtube_window.grab_set()

    # # Create and place a label and entry for YouTube URL
    youtube_url_label = Label(youtube_window, text="YouTube URL:")
    youtube_url_label.grid(row=0, column=0)
    youtube_url_entry = Entry(youtube_window, width=50)
    youtube_url_entry.grid(row=0, column=1)
    # youtube_url = youtube_url_entry.get()

    # # Create and place an Import button
    import_button = Button(youtube_window, text="Import", command=lambda: handle_import(youtube_url_entry))
    import_button.grid(row=1, column=1)

    # When the top-level window is destroyed, re-enable the main window
    # youtube_window.protocol("WM_DELETE_WINDOW", lambda: on_close(youtube_window))


def on_close(window_input):
    """Handle the closing of the top-level window."""
    window_input.destroy()  # Close the top-level window
    window_input.master.attributes('-disabled', False)  # Re-enable the main window


def handle_import(url_entry):
    youtube_url = url_entry.get()
    youtube_handler = MediaProcessor(youtube_url=youtube_url)
    words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
    # print(words_list)
    # print(definition_list)
    # # print(type(words_list))

    words_saver(words_list, definition_list)


###################### Main Window #######################
window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)


menu_bar = Menu(window)
window.config(menu=menu_bar)

import_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Import", menu=import_menu)

youtube_icon_img = PhotoImage(file="./data/images/youtube-icon-2.png")
import_menu.add_command(label="YouTube", image=youtube_icon_img, compound="left", command=youtube_import_from_menu)

# export_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Export", menu=export_menu)

# Main Canvas for showing words and meanings in the App
canvas_manager = CanvasManager()
canvas_manager.create_canvas()

# Main Buttons and their functionality
button_manager = ButtonManager(window, canvas_manager)
button_manager.create_buttons()



window.mainloop()


