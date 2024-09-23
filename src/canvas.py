from tkinter import Canvas, PhotoImage
from word_repository import WordRepoManager
from app_config import (
    CARD_FRONT_IMAGE_PATH,
    CARD_BACK_IMAGE_PATH,
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    BACKGROUND_COLOR,
    CANVAS_Highlight_Thickness,
    CANVAS_IMAGE_SIZE,
    CANVAS_DEFINITION_POSITION,
    CANVAS_DEFINITION_FONT,
    CANVAS_DEFINITION_WIDTH,
    CANVAS_WORD_POSITION,
    CANVAS_WORD_FONT,
    CANVAS_WORD_WIDTH,
    CANVAS_GRID_POSITION,
)

class CanvasManager:
    """
    A class to manage the main canvas showing the text of the word and its definition.

    Attributes:
        word_repo_manager (WordRepoManager): Takes an instance of WordRepoManager as an argument. 
    """
    def __init__(self, word_repo_manager: WordRepoManager):
        self.word_repo_manager: WordRepoManager = word_repo_manager
        self.word_text: str = self.word_repo_manager.word_text
        self.canvas: Canvas | None = None
        self.canvas_image: int | None = None
        self.canvas_definition: int | None = None
        self.canvas_word: int | None= None
        self.front_img: PhotoImage = PhotoImage(file=CARD_FRONT_IMAGE_PATH)
        # self.back_img = PhotoImage(file="./data/images/card_back.png")

    def create_canvas(self) -> None:
        """
        Creates the canvas and sets the word and definition texts.
        """
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