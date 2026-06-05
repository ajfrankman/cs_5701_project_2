import numpy as np
import random
import time
from board_utils import Board
from abc import ABC, abstractmethod

MAX_SCORE = 1.0
MIN_SCORE = -1.0
DEPTH_WEIGHT = .00001

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
        self.min_player_number = 1 if player_number == 2 else 2
        self.beta_boundary = float('inf')

        self.total_states_explored = 0

    def get_move(self, board: Board):
        # At the top level, alpha keeps getting more and more updated
        # with the highest score. Every loop it gets passed down. 
        best_move = None # best column
        valid_moves = board.get_valid_moves()
        alpha = float('-inf')

        for move in valid_moves:
            next_board = board.copy()
            next_board.drop_piece(move, self.player_number)
            value = self._min_move(next_board, 1, alpha, self.beta_boundary)
            if value > alpha:
                alpha = value
                best_move = move
        
        return best_move

    def _min_move(self, board: Board, current_depth: int, alpha: float, beta: float):
        # Note for the programmer to help my keep my sanity:
        # I got rid of min_val. Because we check if the board is full, we are
        # guaranteed to update beta at least once before returning it because in
        # connect 4 there is always a valid move if it isn't a tie.
        self.total_states_explored += 1
        if board.check_win(self.player_number):
            # By subtracting the depth weight, we make deep wins less valuable than 
            # shallow (sooner) wins. 
            return MAX_SCORE - (current_depth * DEPTH_WEIGHT)
        if board.board_is_full():
            return 0
        if current_depth == self.max_depth:
            return board.get_score(player_num=self.player_number)
        
        valid_moves = board.get_valid_moves()
        for next_move in valid_moves:
            next_board = board.copy()
            next_board.drop_piece(next_move, self.min_player_number)
            value = self._max_move(next_board, current_depth+1, alpha, beta)
            beta = min(beta, value)
            if beta <= alpha: break
        
        return beta
    
    def _max_move(self, board: Board, current_depth: int, alpha: float, beta: float):
        # No max_val. See note for _minMove
        self.total_states_explored += 1
        if board.check_win(self.min_player_number):
            # By subtracting the depths weight, we make deep losses more favorable than
            # shallow (sooner) losses.
            return MIN_SCORE + (current_depth * DEPTH_WEIGHT)
        if board.board_is_full():
            return 0
        if current_depth == self.max_depth:
            return board.get_score(player_num=self.player_number)
        
        valid_moves = board.get_valid_moves()
        for next_move in valid_moves:
            next_board = board.copy()
            next_board.drop_piece(next_move, self.player_number)
            value = self._min_move(next_board, current_depth+1, alpha, beta)
            alpha = max(alpha, value)
            if alpha >= beta: break
        
        return alpha
