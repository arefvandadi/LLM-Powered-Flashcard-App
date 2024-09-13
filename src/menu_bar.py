from tkinter import * 
from media_processor import MediaProcessor
from words_saver import words_saver

MENU_TITLE_1 = "Import"
MENU_TITLE_1_SUB_MENU = "YouTube"
YOUTUBE_FAVICON_PATH = "./data/images/youtube-icon-2.png"

class MenuBarManager:
    def __init__(self, root: Tk):
        self.window = root
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.youtube_icon_img = PhotoImage(file=YOUTUBE_FAVICON_PATH)
        
    def create_menu(self):
        import_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=MENU_TITLE_1, menu=import_menu)

        import_menu.add_command(label=MENU_TITLE_1_SUB_MENU, image=self.youtube_icon_img, compound="left", command=self.youtube_import_from_menu)
    

    ###################### Youtube Importing Menu #######################
    def youtube_import_from_menu(self):
        """
        Opens a new window if Import/YouTube in the menu bar is clicked. 
        Provides a url entry for user to enter the YouTube url.

        Returns:
        ----------
        None
        """
        # Create a new top-level window
        youtube_window = Toplevel(self.window, padx=20, pady=20)
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
        import_button = Button(youtube_window, text="Import", command=lambda: self.handle_import(youtube_url_entry))
        import_button.grid(row=1, column=1)

        # When the top-level window is destroyed, re-enable the main window
        # youtube_window.protocol("WM_DELETE_WINDOW", lambda: on_close(youtube_window))


    def on_close(self, window_input):
        """Handle the closing of the top-level window."""
        window_input.destroy()  # Close the top-level window
        window_input.master.attributes('-disabled', False)  # Re-enable the main window


    def handle_import(self, url_entry):
        youtube_url = url_entry.get()
        youtube_handler = MediaProcessor(youtube_url=youtube_url)
        words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
        print(words_list)
        print(definition_list)
        # # print(type(words_list))

        words_saver(words_list, definition_list)


