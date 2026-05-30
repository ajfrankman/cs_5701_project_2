from board_utils import Board

def play_game(player_one_func, player_two_func, rows: int = 6, cols: int = 7):
    # Initialize a clean board
    board = Board(rows=rows, cols=cols)
    
    # Map turn numbers to the respective player logic
    # Player 1 uses player_one_func, Player 2 uses player_two_func
    player_logic = {1: player_one_func, 2: player_two_func}
    
    current_player = 1
    game_over = False
    
    # Draw initial clean board state
    board.show_board()
    
    while not game_over:
        print(f"\n--- Player {current_player}'s Turn ---")
        # The engine calls the function mapped to the current player.
        get_move = player_logic[current_player]
        chosen_col = get_move(board)

        if not board.drop_piece(chosen_col, player=current_player):
            print("That column is full! Try again.")
            continue
        
        # 3. SHOW STATE
        board.show_board()
        
        # 4. CHECK CONDITIONS
        if board.check_win(current_player):
            print(f"\n🎉 PLAYER {current_player} WINS THE GAME! 🎉")
            game_over = True
        elif board.board_is_full(): # Board is completely full with no spaces
            print("\n🤝 It's a draw! Board is full. 🤝")
            game_over = True
            
        # 5. SWITCH TURNS
        current_player = 2 if current_player == 1 else 1
