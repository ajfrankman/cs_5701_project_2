import numpy as np
import random
import time
from board_utils import Board

def human_player(board: Board):
    """Asks a human for a column via terminal input."""
    while True:
        try:
            max_col_indexes = board.max_cols
            col = int(input(f"Choose a column (1-{max_col_indexes}): "))
            if 1 <= col <= max_col_indexes:
                return col-1
            print(f"Invalid column! Must be between 1 and {max_col_indexes}.")
        except ValueError:
            print("Please enter a valid integer.")

def ai_random_player(board: Board):
    """A placeholder AI that just picks a random valid column."""
    # Find columns that aren't full (Row 5 is empty)
    valid_columns = [col for col in range(board.max_cols) if board.grid[board.max_rows-1, col] == 0]
    
    return random.choice(valid_columns)