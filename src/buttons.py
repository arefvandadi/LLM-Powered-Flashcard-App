from tkinter import *
import pandas as pd
from canvas import CanvasManager

BACKGROUND_COLOR = "#B1DDC6"

SHOW_ANSWER_BUTTON_TEXT = "show answer"
SHOW_ANSWER_BACKGROUND_COLOR = "#00ac00"

WRONG_BUTTON_PATH = "./data/images/wrong.png"
RIGHT_BUTTON_PATH = "./data/images/right.png"

HIGHLIGHT_THICKNESS = 0

class ButtonManager:
    """
    A Class to handle the generations and functionality of all button of the GUI

    Attributes:
        root (Tk): An instance of Tk class from tkinter 
    """
    
    def __init__(self, root: Tk, canvas_manager: CanvasManager):
        super().__init__()
        self.window = root
        self.canvas_manager = canvas_manager
        self.definition_text = None
        self.new_word_text = None
    
    def create_buttons(self):
        # Wrong Button
        wrong_img = PhotoImage(file=WRONG_BUTTON_PATH)
        self.wrong_button = Button(self.window, 
                              image=wrong_img, 
                              bg=BACKGROUND_COLOR, 
                              highlightthickness=HIGHLIGHT_THICKNESS, 
                              command=self.wrong_button_functionality)
        # wrong_button.grid(row=1, column=1)

        # Right Button
        right_img = PhotoImage(file=RIGHT_BUTTON_PATH)
        self.right_button = Button(self.window, 
                              image=right_img, 
                              bg=BACKGROUND_COLOR, 
                              highlightthickness=HIGHLIGHT_THICKNESS, 
                              command=self.right_button_functionality)
        # right_button.grid(row=1, column=4)

        # Show Answer Button
        self.showanswer_button = Button(self.window, 
                                   text=SHOW_ANSWER_BUTTON_TEXT,
                                   bg=BACKGROUND_COLOR, 
                                   highlightthickness=HIGHLIGHT_THICKNESS, 
                                   command=self.show_answer)
        
        self.showanswer_button.config(
            width=30, height=3, 
            font=("Arial",20, "bold"), 
            background=SHOW_ANSWER_BACKGROUND_COLOR, 
            activebackground=SHOW_ANSWER_BACKGROUND_COLOR)
        self.showanswer_button.grid(row=1, column=2, columnspan=2)
        self.window.bind("<space>",self.show_answer)
    

    ###################### Setting Word Text When Wrong and Right Buttons are Clicked ######################
    # def set_word_text_when_wrong_and_right_buttons_clicked(self, word_text: str):
    #     self.word_text = word_text


    ###################### Wrong Button Functionality ######################
    def wrong_button_functionality(self, event=None):

        # Ask CanvasManager's word_retriever method to pick a new word from word_repo
        self.canvas_manager.word_retriver()    

        # Bring Show Answer Button back on
        self.showanswer_button.grid(row=1, column=2, columnspan=2)
        
        # Hide Right and Wrong Buttons
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

        self.set_word_text_when_wrong_and_right_buttons_clicked()
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_word, text=self.canvas_manager.word_text, font=("Arial",30, "bold"))
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=f"")

        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.unbind("<m>")
        self.window.bind("<space>", self.show_answer)


    ###################### Right Button Functionality ######################
    def right_button_functionality(self, event=None):
        
        # Ask CanvasManager's word_retriever method to pick a new word from word_repo
        self.canvas_manager.word_retriver()

        # Bring Show Answer Button back on
        self.showanswer_button.grid(row=1, column=2, columnspan=2)
        
        # Hide Right and Wrong Buttons
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_word, text=self.canvas_manager.word_text, font=("Arial",30, "bold"))
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=f"")

        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.unbind("<m>")
        self.window.bind("<space>", self.show_answer)

    
    ###################### Set Definition text when Show Answer button is clicked ######################
    # def set_definition_text_when_show_answer_button_is_clicked(self, definition_text: str):
    #     self.definition_text = definition_text

    
    ###################### Show Answer Function ######################
    def show_answer(self, event=None):
        # Hide the Show Answer Button
        self.showanswer_button.grid_forget()
        
        # Bring Right and Wrong Buttons back on
        self.wrong_button.grid(row=1, column=2)
        self.right_button.grid(row=1, column=3)

        #
        # canvas.itemconfig(canvas_word, text=f"{words_repo.iloc[0,1]}", font=("Arial",30, "bold"))
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=self.canvas_manager.definition_text)

        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.bind("<space>", self.right_button_functionality)
        self.window.bind("<m>", self.wrong_button_functionality)
    
    
