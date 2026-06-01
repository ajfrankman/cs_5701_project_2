from board_utils import Board
from players import Player

def play_game(player_one: Player, player_two: Player, rows: int = 6, cols: int = 7):
    # Initialize a clean board
    board = Board(rows=rows, cols=cols)
    
    # Map turn numbers to the respective player logic
    # Player 1 uses player_one_func, Player 2 uses player_two_func
    player_move_func = {1: player_one.get_move, 2: player_two.get_move}
    
    current_player_num = 1
    game_over = False
    
    # Draw initial clean board state
    board.show_board()
    
    while not game_over:
        print(f"\n--- Player {current_player_num}'s Turn ---")
        # The engine calls the function mapped to the current player.
        get_move = player_move_func[current_player_num]
        chosen_col = get_move(board)

        if not board.drop_piece(chosen_col, player=current_player_num):
            print("That column is full! Try again.")
            continue
        
        # 3. SHOW STATE
        board.show_board()
        
        # 4. CHECK CONDITIONS
        if board.check_win(current_player_num):
            print(f"\n🎉 PLAYER {current_player_num} WINS THE GAME! 🎉")
            game_over = True
        elif board.board_is_full(): # Board is completely full with no spaces
            print("\n🤝 It's a draw! Board is full. 🤝")
            game_over = True
            
        # 5. SWITCH TURNS
        current_player_num = 2 if current_player_num == 1 else 1
