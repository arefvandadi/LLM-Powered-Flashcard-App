from media_processor import MediaProcessor
from words_saver import words_saver
from tkinter import * 
import pandas as pd

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
words_repo = pd.read_csv("./data/words/words_to_learn.csv")
# print(words_repo.iloc[0,0])
# print(words_repo.iloc[0,1])
# print(words_repo.columns[0])

###################### RWrong Button Functionality ######################
def wrong_button_functionality(event=None):
    # Bring Show Answer Button back on
    showanswer_button.grid(row=1, column=2, columnspan=2)
    
    # Hide Right and Wrong Buttons
    wrong_button.grid_forget()
    right_button.grid_forget()

    canvas.itemconfig(canvas_word, text=f"{words_repo.iloc[0,0]}", font=("Arial",30, "bold"))
    canvas.itemconfig(canvas_definition, text=f"")

    window.unbind("<space>")
    window.unbind("<m>")
    window.bind("<space>", show_answer)


###################### Right Button Functionality ######################
def right_button_functionality(event=None):
    # Bring Show Answer Button back on
    showanswer_button.grid(row=1, column=2, columnspan=2)
    
    # Hide Right and Wrong Buttons
    wrong_button.grid_forget()
    right_button.grid_forget()

    canvas.itemconfig(canvas_word, text=f"{words_repo.iloc[0,0]}", font=("Arial",30, "bold"))
    canvas.itemconfig(canvas_definition, text=f"")

    window.unbind("<space>")
    window.unbind("<m>")
    window.bind("<space>", show_answer)

###################### Show Answer Function ######################
def show_answer(event=None):
    # Hide the Show Answer Button
    showanswer_button.grid_forget()
    
    # Bring Right and Wrong Buttons back on
    wrong_button.grid(row=1, column=2)
    right_button.grid(row=1, column=3)

    #
    # canvas.itemconfig(canvas_word, text=f"{words_repo.iloc[0,1]}", font=("Arial",30, "bold"))
    canvas.itemconfig(canvas_definition, text=f"{words_repo.iloc[0,1]}")

    window.unbind("<space>")
    window.bind("<space>", right_button_functionality)
    window.bind("<m>", wrong_button_functionality)

###################### Main Window #######################
window = Tk()
window.title("FlashMind")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

# Main Canvas for showing words and meanings in the App
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas_definition = canvas.create_text(400, 150, text=f"", font=("Arial",15), width=500)
canvas_word = canvas.create_text(400, 50, text=f"{words_repo.iloc[0,0]}", font=("Arial",30, "bold"), width=500)
canvas.grid(row=0, column=0, columnspan=6)

# Wrong Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(window, image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button_functionality)
# wrong_button.grid(row=1, column=1)

# Right Button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(window, image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button_functionality)
# right_button.grid(row=1, column=4)

# Show Answer Button
showanswer_button = Button(window, text="show answer",bg=BACKGROUND_COLOR, highlightthickness=0, command=show_answer)
showanswer_button.config(
    width=30, height=3, 
    font=("Arial",20, "bold"), 
    background=SHOW_ANSWER_BACKGROUND_COLOR, 
    activebackground=SHOW_ANSWER_BACKGROUND_COLOR)
showanswer_button.grid(row=1, column=2, columnspan=2)
window.bind("<space>",show_answer)







window.mainloop()


