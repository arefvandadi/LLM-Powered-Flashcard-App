from tkinter import Canvas, PhotoImage
import pandas as pd 
import random

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

CANVAS_GRID_POSITION = (0, 0, 6)


class CanvasManager:
    def __init__(self):
        self.canvas = None
        self.canvas_image = None
        self.canvas_definition = None
        self.canvas_word = None
        self.front_img = PhotoImage(file="./data/images/card_front.png")
        self.back_img = PhotoImage(file="./data/images/card_back.png")
        self.word_text = None
        self.definition_text = None

    def create_canvas(self):
        self.word_retriver()
        self.canvas = Canvas(width=CANVAS_WIDTH, 
                        height=CANVAS_HEIGHT, 
                        bg=BACKGROUND_COLOR, 
                        highlightthickness=CANVAS_Highlight_Thickness)
        self.canvas_image = self.canvas.create_image(CANVAS_IMAGE_SIZE[0], 
                                           CANVAS_IMAGE_SIZE[1], 
                                           image=self.front_img)
        self.canvas_definition = self.canvas.create_text(self._DEFINITION_POSITION[0], 
                                               CANVAS_DEFINITION_POSITION[1], 
                                               text="", 
                                               font=CANVAS_DEFINITION_FONT, 
                                               width=CANVAS_DEFINITION_WIDTH)
        self.canvas_word = self.canvas.create_text(CANVAS_WORD_POSITION[0], 
                                         CANVAS_WORD_POSITION[1], 
                                         text=self.word_text, 
                                         font=CANVAS_WORD_FONT, 
                                         width=CANVAS_WORD_WIDTH)
        self.canvas.grid(row=CANVAS_GRID_POSITION[0], 
                    column=CANVAS_GRID_POSITION[1], 
                    columnspan=CANVAS_GRID_POSITION[2])
    

    def word_retriver(self):
        word_repo = pd.read_csv("./data/words/words_to_learn.csv")
        word_repo_length = word_repo.shape[0]
        random_row = random.randint(0, word_repo_length-1)
        self.word_text = word_repo.iloc[random_row,1]
        self.definition_text = word_repo.iloc[random_row,2]



# # Main Canvas for showing words and meanings in the App
# front_img = PhotoImage(file="./data/images/card_front.png")
# back_img = PhotoImage(file="./data/images/card_back.png")
# canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas_image = canvas.create_image(400, 263, image=front_img)
# canvas_definition = canvas.create_text(400, 150, text=f"", font=("Arial",15), width=500)
# canvas_word = canvas.create_text(400, 50, text=f"{words_repo.iloc[0,0]}", font=("Arial",30, "bold"), width=500)
# canvas.grid(row=0, column=0, columnspan=6)