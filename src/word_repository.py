from tkinter import *
import pandas as pd
import random
from config import (
    BACKGROUND_COLOR,
    WORDS_REPO_DESTINATION_FOLDER,
    WORD_REPO_NAME
)

class WordRepoManager:
    """
    A class to handle all the interactions with the word repository.

    Provides methods to do the following:
        - Calculate the current number of words in word repository.
        - Selects a new word from the word repository
        - Remove a word from the repositry
        - Updates the word repository when the main window of the App is closed.
        - Saves new words imported from youtueb into the word repository.
    
    Attributes:
        window (Tk): An instance of the Tk class i.e. the main window of the app.
    
    """
    def __init__(self, root: Tk):
        self.window = root
        self.word_repo = pd.read_csv(WORDS_REPO_DESTINATION_FOLDER + WORD_REPO_NAME)
        self.word_repo_length = self.word_repo.shape[0]
        self.random_row = random.randint(0, self.word_repo_length-1)
        self.word_text = self.word_repo.iloc[self.random_row,0]
        self.definition_text = self.word_repo.iloc[self.random_row,1]
        self.words_remaining_label = Label(self.window, text=f"Words Remaining: {self.word_repo_length}", font=("Arial", 10, "bold"), bg=BACKGROUND_COLOR, pady=10)
        self.words_remaining_label.grid(row=0, column=2, columnspan=2)
        

    def calculate_number_of_words_in_word_repo(self):
        """
        Calculates the current number of words in the word repository.
        Updates the Word Remaining label on the GUI.

        Returns:
        -----------
        None
        """
        self.word_repo_length = self.word_repo.shape[0]
        self.words_remaining_label.config(text=f"Words Remaining: {self.word_repo_length}")

    def word_retriver(self):
        """
        Randomly selects a word and its definition from the repository.
        It is tied to Wrong and Right buttons' functions so that a new word is shown upon pressing these two buttons. 

        Returns:
        -----------
        None
        """
        self.word_repo_length = self.word_repo.shape[0]
        self.random_row = random.randint(0, self.word_repo_length-1)
        self.word_text = self.word_repo.iloc[self.random_row,0]
        self.definition_text = self.word_repo.iloc[self.random_row,1]

    def word_remover(self):
        """
        Removes a word from the word repository. 
        It is tied to Right button function so the word that is guessed correctly be removed. 

        Returns:
        -----------
        None
        """
        self.word_repo.drop(index=self.random_row, inplace=True)
        self.word_repo = self.word_repo.reset_index(drop=True)
    
    def update_word_repo_csv(self, words_repo_destination_folder=WORDS_REPO_DESTINATION_FOLDER):
        """
        Updates the word repository when the Flashcard App main window is closed.

        Returns:
        -----------
        None
        """
        self.word_repo.to_csv(words_repo_destination_folder + WORD_REPO_NAME, index=False)
        self.window.destroy()
    
    def words_saver(self, word_list: list, definition_list: list):
        """
        Takes a python list of new words and a python list of corresponding definitions 
        and adds them to the word repository

        Returns:
        ---------
        None
        """
        if len(word_list) != len(definition_list):
            print("Error:", "The number of words and definitions does not match. No words were added.")

            return #Nothing is returned. Exit the function.

        new_pd = pd.DataFrame({"English":word_list})
        new_pd["Definition"] = definition_list

        #Add the new words and definitions to the main word repository Dataframe and drop the duplicates
        self.word_repo = pd.concat([self.word_repo, new_pd], axis=0, ignore_index=True).drop_duplicates("English")
        
        # Update the Word Remaining label on GUI
        self.calculate_number_of_words_in_word_repo()