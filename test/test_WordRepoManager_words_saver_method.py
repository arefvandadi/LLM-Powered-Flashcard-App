import pytest
import pandas as pd
from unittest.mock import MagicMock
from tkinter import Tk
from ..src.word_repository import WordRepoManager

# Creates a Mock instace of the Tk() class in tkinter module.
@pytest.fixture
def mock_tk():
    """Fixture to provide a mock Tk instance."""
    return MagicMock(spec=Tk)

# Create a mock Dataframe to avoid using pd.read_csv in the WordRepoManager class attributes.
@pytest.fixture
def mock_word_repo_manager(mock_tk):
    """Fixture to provide a WordRepoManager instance with mocked dependencies."""
    # Create a mock CSV DataFrame
    mock_df = pd.DataFrame({
        "English": ["cat", "dog"],
        "Definition": ["a small domesticated carnivorous mammal", "a domesticated carnivorous mammal"]
    })
    
    # Mock pd.read_csv to return the mock DataFrame
    with pytest.MonkeyPatch.context() as m:
        # replaces pd.read_csv() method used inside WordRepoManager class with a mock DataFrame  defined above
        m.setattr(pd, "read_csv", lambda _: mock_df)
        manager = WordRepoManager(mock_tk)
        yield manager

def test_words_saver_saving_words_correctly(mock_word_repo_manager):
    """Test if words and definitions are saved correctly."""
    manager = mock_word_repo_manager
    new_words = ["fish", "bird"]
    new_definitions = ["an aquatic animal", "a flying animal"]
    manager.words_saver(new_words, new_definitions)

    expected_repo = pd.DataFrame({
        "English": ["cat", "dog", "fish", "bird"],
        "Definition": ["a small domesticated carnivorous mammal", "a domesticated carnivorous mammal", "an aquatic animal", "a flying animal"]
    })

    pd.testing.assert_frame_equal(manager.word_repo, expected_repo)