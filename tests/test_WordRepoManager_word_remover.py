import pytest
import pandas as pd
from unittest.mock import MagicMock
from tkinter import Tk
from app_config import *
from src.word_repository import WordRepoManager
# from word_repository import WordRepoManager

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


def test_word_remover(mock_word_repo_manager):
    manager = mock_word_repo_manager
    radom_word = manager.word_text

    manager.word_remover()

    assert radom_word not in manager.word_repo["English"].values, "word is still in the word repository"