from tkinter import Tk
from ui.canvas import CanvasManager
from ui.buttons import ButtonManager
from ui.menu_bar import MenuBarManager
from services.media_processor import MediaProcessor
from services.word_repository import WordRepoManager
from config.app_config import BACKGROUND_COLOR

def main():

    ###################### Main Window #######################
    window = Tk()
    window.title("FlashMind")
    window.config(padx=50, pady=50)
    window.config(bg=BACKGROUND_COLOR)

    # Word Repository Manager
    word_repo_manager = WordRepoManager(window)

    # Main Canvas for showing words and meanings in the App
    canvas_manager = CanvasManager(word_repo_manager)
    canvas_manager.create_canvas()

    # Main Buttons and their functionality
    button_manager = ButtonManager(window, canvas_manager, word_repo_manager)
    button_manager.create_buttons()

    # Create Manu Bar and Handle Importing Words by Using media_processor and words_saver modules
    menu_bar_manager = MenuBarManager(window, MediaProcessor, canvas_manager, button_manager)
    menu_bar_manager.create_menu()


    # Changes the closing protocol of the app window. 
    # It binds the actions of closing the window with the update_word_repo_csv method in word_repository module. 
    window.protocol("WM_DELETE_WINDOW", word_repo_manager.update_word_repo_csv)

    window.mainloop()


if __name__ == "__main__":
    main()
