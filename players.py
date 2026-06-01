import numpy as np
import random
import time
from board_utils import Board
from abc import ABC, abstractmethod

MAX_SCORE = 1.0
MIN_SCORE = -1.0

class Player(ABC):

    def __init__(self, player_number):
        self.player_number = player_number

    @abstractmethod
    def get_move(self, board: Board):
        pass

class Human(Player):

    def get_move(self, board: Board):
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

class RandomAI(Player):
    
    def __init__(self, player_number):
        self.player_number = player_number
    
    def get_move(self, board: Board):
        """A placeholder AI that just picks a random valid column."""
        # Find columns that aren't full (Row 5 is empty)
        valid_columns = [col for col in range(board.max_cols) if board.grid[board.max_rows-1, col] == 0]
        
        return random.choice(valid_columns)

class MiniMaxAI(Player):

    def __init__(self, player_number: int, max_depth: int = 3):
        # Use super() to let the parent template handle name and piece_id
        super().__init__(player_number=player_number)
        # Add variables unique ONLY to the AI
        self.max_depth = max_depth

    def get_move(self, board: Board):
        best_move = None # best column
        best_so_far = float('-inf') # Best value from move
        valid_moves = board.get_valid_moves()
        debug_dict = {}
        for move in valid_moves:
            value = self._maxMove(self.player_number, board, move, 1)
            debug_dict[move] = value
            if value > best_so_far:
                best_so_far = value
                best_move = move
        return best_move

    def _minMove(self, player_num: int, board: Board, move: int, current_depth: int):
        other_player_num = 1 if player_num == 2 else 2
        board_copy = board.copy()
        board_copy.drop_piece(move, player_num)
        if board_copy.check_win(player_num):
            return MIN_SCORE
        if board_copy.board_is_full():
            return 0
        if current_depth == self.max_depth:
            return board_copy.get_score(player_num=self.player_number)
        min_val = MAX_SCORE
        valid_moves = board_copy.get_valid_moves()
        for next_move in valid_moves:
            value = self._maxMove(other_player_num, board_copy, next_move, current_depth+1)
            if value < min_val:
                min_val = value
        return min_val
    
    def _maxMove(self, player_num: int, board: Board, move: int, current_depth: int):
        other_player_num = 1 if player_num == 2 else 2
        board_copy = board.copy()
        board_copy.drop_piece(move, player_num)
        if board_copy.check_win(player_num):
            return MAX_SCORE
        if board_copy.board_is_full():
            return 0
        if current_depth == self.max_depth:
            return board_copy.get_score(player_num=self.player_number)
        max_val = MIN_SCORE
        valid_moves = board_copy.get_valid_moves()
        for next_move in valid_moves:
            value = self._minMove(other_player_num, board_copy, next_move, current_depth+1)
            if value > max_val:
                max_val = value
        return max_val
