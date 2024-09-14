from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

class WordRepoManager:
    def __init__(self, root: Tk):
        self.window = root
        self.word_repo = pd.read_csv("./data/words/words_to_learn.csv")
        self.word_repo_length = self.word_repo.shape[0]
        self.random_row = random.randint(0, self.word_repo_length-1)
        self.word_text = self.word_repo.iloc[self.random_row,0]
        self.definition_text = self.word_repo.iloc[self.random_row,1]
        # self.words_remaining_counter = self.word_repo_length
        self.words_remaining_label = Label(self.window, text=f"Words Remaining: {self.word_repo_length}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR, pady=10)
        self.words_remaining_label.grid(row=0, column=2, columnspan=2)
        

    def calculate_number_of_words_in_word_repo(self):
        self.word_repo_length = self.word_repo.shape[0]
        self.words_remaining_label.config(text=f"Words Remaining: {self.word_repo_length}")

    def word_retriver(self):
        # self.word_repo = pd.read_csv("./data/words/words_to_learn.csv") # Not Needed. Add an Update Repo fucntion 
        self.word_repo_length = self.word_repo.shape[0]
        self.random_row = random.randint(0, self.word_repo_length-1)
        self.word_text = self.word_repo.iloc[self.random_row,0]
        self.definition_text = self.word_repo.iloc[self.random_row,1]

    def word_remover(self):
        self.word_repo.drop(index=self.random_row, inplace=True)
        self.word_repo = self.word_repo.reset_index(drop=True)
    
    def update_word_repo_csv(self):
        self.word_repo.to_csv("./data/words/words_to_learn.csv", index=False)
        self.window.destroy()
    
    def words_saver(self, word_list: list, definition_list: list, words_destination_path: str="./data/words/"):
        """
        Takes a python list of new words and adds them to the words_to_learn.csv

        Returns:
        ---------
        None
        """
    
        # Read in the main word repository csv file as a dataframe
        # words_Dataframe = pd.read_csv(words_destination_path + "words_to_learn.csv")
        # Creating a new dataframe from the new words and definitions python list
        # new_pd = pd.DataFrame({"English":word_list, "Definition":definition_list})
        new_pd = pd.DataFrame({"English":word_list})
        new_pd["Definition"] = definition_list

        #Add the new words and definitions to the main word repository Dataframe and drop the duplicates
        self.word_repo = pd.concat([self.word_repo, new_pd], axis=0, ignore_index=True).drop_duplicates("English")
        
        # Update the Word Remaining label on GUI
        self.calculate_number_of_words_in_word_repo()