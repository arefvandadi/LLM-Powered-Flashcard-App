from tkinter import *
from canvas import CanvasManager
from word_repository import WordRepoManager

BACKGROUND_COLOR = "#B1DDC6"

SHOW_ANSWER_BUTTON_TEXT = "show answer"
SHOW_ANSWER_BACKGROUND_COLOR = "#00ac00"
SHOW_ANSWER_BUTTON_GRID = {'row': 2, 'column': 2, 'columnspan': 2}

WRONG_BUTTON_PATH = "./data/images/wrong.png"
WRONG_BUTTON_GRID = {'row': 2, 'column': 2}
RIGHT_BUTTON_PATH = "./data/images/right.png"
RIGHT_BUTTON_GRID = {'row': 2, 'column': 3}

HIGHLIGHT_THICKNESS = 0

class ButtonManager:
    """
    A Class to handle the generations and functionality of all button of the GUI

    Attributes:
        root (Tk): An instance of Tk class from tkinter 
    """
    
    def __init__(self, root: Tk, canvas_manager: CanvasManager, word_repo_manager: WordRepoManager):
        self.window = root
        self.canvas_manager = canvas_manager
        self.word_repo_manager = word_repo_manager
        self.wrong_img = PhotoImage(file="./data/images/wrong.png")
        self.right_img = PhotoImage(file="./data/images/right.png")
    
    def create_buttons(self):
        # Wrong Button
        self.wrong_button = Button(self.window, 
                              image=self.wrong_img, 
                              bg=BACKGROUND_COLOR, 
                              highlightthickness=HIGHLIGHT_THICKNESS, 
                              command=self.wrong_button_functionality)

        # Right Button
        self.right_button = Button(self.window, 
                              image=self.right_img, 
                              bg=BACKGROUND_COLOR, 
                              highlightthickness=HIGHLIGHT_THICKNESS, 
                              command=self.right_button_functionality)

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
        self.showanswer_button.grid(**SHOW_ANSWER_BUTTON_GRID)
        self.window.bind("<space>",self.show_answer)


    ###################### Wrong Button Functionality ######################
    def wrong_button_functionality(self, event=None):

        # Ask CanvasManager's word_retriever method to pick a new word from word_repo
        self.word_repo_manager.word_retriver()

        # Bring Show Answer Button back on
        self.showanswer_button.grid(**SHOW_ANSWER_BUTTON_GRID)
        
        # Hide Right and Wrong Buttons
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

        # self.set_word_text_when_wrong_and_right_buttons_clicked()
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_word, text=self.word_repo_manager.word_text, font=("Arial",30, "bold"))
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=f"")

        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.unbind("<m>")
        self.window.bind("<space>", self.show_answer)


    ###################### Right Button Functionality ######################
    def right_button_functionality(self, event=None):
        
        # Remove the correctly guessed word from the word repo
        self.word_repo_manager.word_remover()

        #Update Word Remaining Label
        self.word_repo_manager.calculate_number_of_words_in_word_repo()

        # Ask CanvasManager's word_retriever method to pick a new word from word_repo
        self.word_repo_manager.word_retriver()

        # Bring Show Answer Button back on
        self.showanswer_button.grid(**SHOW_ANSWER_BUTTON_GRID)
        
        # Hide Right and Wrong Buttons
        self.wrong_button.grid_forget()
        self.right_button.grid_forget()

        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_word, text=self.word_repo_manager.word_text, font=("Arial",30, "bold"))
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=f"")

        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.unbind("<m>")
        self.window.bind("<space>", self.show_answer)

    
    ###################### Show Answer Function ######################
    def show_answer(self, event=None):
        # Hide the Show Answer Button
        self.showanswer_button.grid_forget()

        # Bring Right and Wrong Buttons back on
        self.wrong_button.grid(**WRONG_BUTTON_GRID)
        self.right_button.grid(**RIGHT_BUTTON_GRID)
 
        # Shows the meaning of the word on canvas when Show Answer button is pressed.
        self.canvas_manager.canvas.itemconfig(self.canvas_manager.canvas_definition, text=self.word_repo_manager.definition_text)
  
        # Binding and unbinding Keyboard Keys
        self.window.unbind("<space>")
        self.window.bind("<space>", self.right_button_functionality)
        self.window.bind("<m>", self.wrong_button_functionality)