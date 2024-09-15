import pytest
import pandas as pd
from unittest.mock import MagicMock
from tkinter import Tk
from src.word_repository import WordRepoManager

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
    root.destroy()



# Test function to evaluate how the new words are concatenated into the word repository
def test_words_saver_saving_words_correctly(mock_word_repo_manager):
    """Test if words and definitions are saved correctly."""
    manager = mock_word_repo_manager
    new_words = ["devalued", "retain"]
    new_definitions = ["Reduced in worth or value.", "to keep or hold onto something"]
    manager.words_saver(new_words, new_definitions)

    expected_repo = pd.DataFrame({
        "English": ["Liberty", "poll", "devalued", "retain"],
        "Definition": ["the state of being free within society", "a survey of public opinion", "Reduced in worth or value.", "to keep or hold onto something"]
    })

    pd.testing.assert_frame_equal(manager.word_repo, expected_repo)