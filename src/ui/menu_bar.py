from tkinter import * 
from services.media_processor import MediaProcessor
from ui.buttons import ButtonManager
from ui.canvas import CanvasManager
from services.word_repository import WordRepoManager
from config.app_config import (
    MENU_TITLE_1,
    MENU_TITLE_1_SUB_MENU,
    YOUTUBE_FAVICON_PATH,
    YOUTUBE_URL_LABEL_GRID,
    YOUTUBE_URL_ENTRY_GRID,
    IMPORT_BUTTON_GRID,
    SHOW_ANSWER_BUTTON_GRID,
)

class MenuBarManager:
    """
    A class to manage all related to the Menu bar

    Attributes:
        window (Tk): An instance of Tk class. the main window of the app.
        media_processor (MediaProcessor): An instance of MediaProcessor module.
        word_repo_manager (WordRepoManager): An instance of WordRepoManager module.
    """
    def __init__(self, root: Tk, media_processor: MediaProcessor, canvas_manager: CanvasManager, button_manager: ButtonManager):
        self.window: Tk = root
        self.media_processor: MediaProcessor = media_processor
        self.canvas_manager: CanvasManager = canvas_manager
        self.word_repo_manager: WordRepoManager = self.canvas_manager.word_repo_manager
        self.button_manager: ButtonManager = button_manager
        self.menu_bar: Menu = Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.youtube_icon_img: PhotoImage = PhotoImage(file=YOUTUBE_FAVICON_PATH)
        
    def create_menu(self) -> None:
        import_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=MENU_TITLE_1, menu=import_menu)

        import_menu.add_command(label=MENU_TITLE_1_SUB_MENU, 
                                image=self.youtube_icon_img, 
                                compound="left", 
                                command=self.youtube_import_from_menu)
    

    ###################### Youtube Importing Menu #######################
    def youtube_import_from_menu(self) -> None:
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



    def handle_import(self, url_entry: Entry) -> None:
        """
        Handles everything needed to set the GUI and extract words upon pressing the import button.
        """
        youtube_url = url_entry.get()
        youtube_handler = self.media_processor(youtube_url=youtube_url)
        words_list, definition_list = youtube_handler.extract_words_from_youtube_pipeline()
        print(words_list)
        print(definition_list)
        # # print(type(words_list))
        if self.word_repo_manager.word_repo_length > 0:
            self.word_repo_manager.words_saver(words_list, definition_list)
        
        # This is when there is no words in the word repo and we are importing more words.
        else:
            self.word_repo_manager.words_saver(words_list, definition_list)
            self.word_repo_manager.word_retriver()
            self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_word, text=self.word_repo_manager.word_text, font=("Arial",30, "bold"))
            self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=f"")
            self.button_manager.showanswer_button.grid(**SHOW_ANSWER_BUTTON_GRID)
            self.button_manager.showanswer_button.config(state="normal")


