from tkinter import Canvas, PhotoImage
from word_repository import WordRepoManager

CARD_FRONT_IMAGE_PATH = "./data/images/card_front.png"
CARD_BACK_IMAGE_PATH = "./data/images/card_back.png"

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_Highlight_Thickness = 0

CANVAS_IMAGE_SIZE = (400, 263)

CANVAS_DEFINITION_POSITION = (400, 150)
CANVAS_DEFINITION_FONT = ("Arial",15)
CANVAS_DEFINITION_WIDTH = 500

CANVAS_WORD_POSITION = (400, 50)
CANVAS_WORD_FONT = ("Arial",30, "bold")
CANVAS_WORD_WIDTH = 500

CANVAS_GRID_POSITION = {'row': 1, 'column': 0, 'columnspan': 6}


class CanvasManager:
    """
    A class to manage the main canvas showing the text of the word and its definition.

    Attributes:
        word_repo_manager (WordRepoManager): Takes an instance of WordRepoManager as an argument. 
    """
    def __init__(self, word_repo_manager: WordRepoManager):
        self.word_repo_manager = word_repo_manager
        self.word_text = self.word_repo_manager.word_text
        self.canvas = None
        self.canvas_image = None
        self.canvas_definition = None
        self.canvas_word = None
        self.front_img = PhotoImage(file=CARD_FRONT_IMAGE_PATH)
        # self.back_img = PhotoImage(file="./data/images/card_back.png")

    def create_canvas(self):
        self.canvas = Canvas(width=CANVAS_WIDTH, 
                        height=CANVAS_HEIGHT, 
                        bg=BACKGROUND_COLOR, 
                        highlightthickness=CANVAS_Highlight_Thickness)
        self.canvas_image = self.canvas.create_image(CANVAS_IMAGE_SIZE[0], 
                                           CANVAS_IMAGE_SIZE[1], 
                                           image=self.front_img)
        self.canvas_definition = self.canvas.create_text(CANVAS_DEFINITION_POSITION[0], 
                                               CANVAS_DEFINITION_POSITION[1], 
                                               text="", 
                                               font=CANVAS_DEFINITION_FONT, 
                                               width=CANVAS_DEFINITION_WIDTH)
        self.canvas_word = self.canvas.create_text(CANVAS_WORD_POSITION[0], 
                                         CANVAS_WORD_POSITION[1], 
                                         text=self.word_text, 
                                         font=CANVAS_WORD_FONT, 
                                         width=CANVAS_WORD_WIDTH)
        self.canvas.grid(**CANVAS_GRID_POSITION)