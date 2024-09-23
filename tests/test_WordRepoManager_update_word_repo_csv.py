# Sets up src folder in sys path
import sys
sys.path.append("./src")

import pytest
import pandas as pd
from tkinter import Tk
import _tkinter
from word_repository import WordRepoManager
import os

WORD_REPO_NAME = "words_to_learn.csv"

@pytest.fixture
def mock_word_repo_manager():
    """Fixture to provide a WordRepoManager instance with a real Tk instance and mocked dependencies."""
    # Create the real Tk instance
    root = Tk()
    
    # Create a mock CSV DataFrame
    mock_df = pd.DataFrame({
        "English": ["Liberty", "poll"],
        "Definition": ["the state of being free within society", "a survey of public opinion"]
    })

    # Mock pd.read_csv to return the mock DataFrame
    with pytest.MonkeyPatch.context() as m:
        m.setattr(pd, "read_csv", lambda _: mock_df)
        manager = WordRepoManager(root)

    # Yield the manager for the test to use
    yield manager

    # Destroy the Tk instance after the test is complete
    # root.destroy()

def test_update_word_repo_csv(mock_word_repo_manager):
    manager = mock_word_repo_manager
    
    temp_folder = "./tests/test_WordRepoManager_update_word_repo_csv/"
    
    # Creates the temp word repository and temp folder
    if not os.path.isdir(temp_folder):
        os.mkdir(temp_folder)

    manager.update_word_repo_csv(words_repo_destination_folder=temp_folder)

    # Check if the file is saved
    assert os.path.isfile(temp_folder + WORD_REPO_NAME), "The file is not created"

    # Check if the content match
    saved_repo = pd.read_csv(temp_folder + WORD_REPO_NAME)
    pd.testing.assert_frame_equal(saved_repo, manager.word_repo)

    # Checks of the window was closed. If it wasm there should be a Tcl Error and the Error message input in match argument below.
    with pytest.raises(_tkinter.TclError, match=r"application has been destroyed"):
        manager.window.winfo_exists()

    # Removes the temp word repository and temp folder
    os.remove(temp_folder + WORD_REPO_NAME)
    os.rmdir(temp_folder)



