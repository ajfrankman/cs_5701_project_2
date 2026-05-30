import numpy as np
import random
from rich.console import Console
from rich.table import Table

class Board:
    # It is important to remember that while a numpy array is technically
    # at (0, 0) in the top left, this was built thinking about it more
    # intuitively: at the bottom left. Then any print or show methods
    # need to remember this before displaying the board.

    def __init__(self, rows: int = 6, cols: int = 7):
        self.max_rows = rows #if rows >=4 else 4
        self.max_cols = cols #if cols >=4 else 4
        self.grid = np.zeros((self.max_rows, self.max_cols), dtype=int)

    def board_is_full(self) -> bool:
        return np.all(self.grid != 0)

    def show_board(self) -> None:
        # Should display the connect four board. 7 col 6 row.
        console = Console()
        table = Table(show_header=False, show_lines=True, border_style="blue")
        
        # Define how our pieces look (0 = empty space, 1 = Red Circle, 2 = Yellow Circle)
        symbols = {0: "  ", 1: "🔴", 2: "🟡"}
        
        # Read from Row 5 down to Row 0 so it prints with correct gravity physics
        for row in range(self.max_rows-1, -1, -1):
            row_cells = [symbols[val] for val in self.grid[row, :]]
            # Unpack python list
            table.add_row(*row_cells)
        
        console.print(table)

    def drop_piece(self, col: int, player: int) -> bool:
        '''
        col = desired column to drop the piece in. zero indexed
        player = either 1 or 2
        returns true if successful.
        '''
        ret_val = False
        # get array of row indices equal to 0
        empty_row_indexes = np.where(self.grid[:, col] == 0)[0]
        if len(empty_row_indexes) > 0:
            ret_val = True
            # bottom row that is still empty
            row = empty_row_indexes[0]
            self.grid[row, col] = player
        return ret_val

    def check_win(self, player) -> bool:
        # Define the 4 directions to check: (row_step, col_step)
        directions = [
            (0, 1),   # Horizontal (Right)
            (1, 0),   # Vertical (Up)
            (1, 1),   # Diagonal (Up-Right)
            (-1, 1)   # Diagonal (Down-Right)
        ]
        
        # Loop through every single slot on the 6x7 grid
        for r in range(self.max_rows):
            for c in range(self.max_cols):
                # If the slot doesn't belong to the player we are checking, skip it
                if self.grid[r, c] != player:
                    continue
                    
                # Check all 4 directions starting from this specific slot [r, c]
                for dr, dc in directions:
                    # Look ahead 1, 2, and 3 steps in this direction
                    # We also don't want to go off the edge of the grid (or wrap
                    # becuase of Python).
                    if r + 3*dr < 0 or c + 3*dc < 0 or r + 3*dr > self.max_rows-1 or c + 3*dc > self.max_cols-1:
                        continue
                        
                    if (self.grid[r + 1*dr, c + 1*dc] == player and
                        self.grid[r + 2*dr, c + 2*dc] == player and
                        self.grid[r + 3*dr, c + 3*dc] == player):
                        return True # Found 4-in-a-row!
        return False # Scanned the whole grid, no win found.
    
    def gen_rand_grid(self, num_checkers: int) -> None:
        player = 1
        num_checkers = 42 if num_checkers > 42 else num_checkers
        for i in range(num_checkers):
            player = player + 1 if player == 1 else player - 1
            drop_success = False
            while not drop_success: # Try until find not full col
                col = random.randint(0, self.max_cols-1)
                drop_success = self.drop_piece(col, player=player)
