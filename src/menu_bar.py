from tkinter import * 
from media_processor import MediaProcessor
from word_repository import WordRepoManager
from config import (
    MENU_TITLE_1,
    MENU_TITLE_1_SUB_MENU,
    YOUTUBE_FAVICON_PATH,
    YOUTUBE_URL_LABEL_GRID,
    YOUTUBE_URL_ENTRY_GRID,
    IMPORT_BUTTON_GRID,
)

class MenuBarManager:
    """
    A class to manage all related to the Menu bar

    Attributes:
        window (Tk): An instance of Tk class. the main window of the app.
        media_processor (MediaProcessor): An instance of MediaProcessor module.
        word_repo_manager (WordRepoManager): AN instance of WordRepoManager module.
    """
    def __init__(self, root: Tk, media_processor: MediaProcessor, word_repo_manager: WordRepoManager):
        self.window = root
        self.media_processor = media_processor
        self.word_repo_manager = word_repo_manager
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.youtube_icon_img = PhotoImage(file=YOUTUBE_FAVICON_PATH)
        
    def create_menu(self):
        import_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=MENU_TITLE_1, menu=import_menu)

        import_menu.add_command(label=MENU_TITLE_1_SUB_MENU, 
                                image=self.youtube_icon_img, 
                                compound="left", 
                                command=self.youtube_import_from_menu)
    

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

        # # Create and place a label and entry for YouTube URL
        youtube_url_label = Label(youtube_window, text="YouTube URL:")
        youtube_url_label.grid(**YOUTUBE_URL_LABEL_GRID)
        youtube_url_entry = Entry(youtube_window, width=50)
        youtube_url_entry.grid(**YOUTUBE_URL_ENTRY_GRID)

        # # Create and place an Import button
        import_button = Button(youtube_window, 
                               text="Import", 
                               command=lambda: self.handle_import(youtube_url_entry))
        import_button.grid(**IMPORT_BUTTON_GRID, padx=10)



    def handle_import(self, url_entry):
        youtube_url = url_entry.get()
        youtube_handler = self.media_processor(youtube_url=youtube_url)
        words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
        print(words_list)
        print(definition_list)
        # # print(type(words_list))

        self.word_repo_manager.words_saver(words_list, definition_list)


