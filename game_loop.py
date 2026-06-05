from board_utils import Board
from players import Player
import time


def play_game(player_one: Player, player_two: Player, rows: int = 6, cols: int = 7):
    # Initialize a clean board
    board = Board(rows=rows, cols=cols)
    
    # Map turn numbers to the respective player logic
    player_move_func = {1: player_one.get_move, 2: player_two.get_move}
    
    metrics = {
            1: {"total_time": 0.0, "max_time": 0, "moves_count": 0, "obj": player_one},
            2: {"total_time": 0.0, "max_time": 0, "moves_count": 0, "obj": player_two}
        }

    current_player_num = 1
    game_over = False
    board.show_board()
    
    while not game_over:
        print(f"\n--- Player {current_player_num}'s Turn ---")
        # The engine calls the function mapped to the current player.
        get_move = player_move_func[current_player_num]

        start_time = time.time()
        chosen_col = get_move(board)
        elapsed_time = time.time() - start_time

        metrics[current_player_num]['total_time'] += elapsed_time
        metrics[current_player_num]['moves_count'] += 1
        metrics[current_player_num]['max_time'] = max(elapsed_time, metrics[current_player_num]['max_time'])

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

    # --- FINAL METRICS REPORT ---
    print("\n=============================================")
    print("         FINAL PERFORMANCE METRICS           ")
    print("=============================================")
    for p_num in [1, 2]:
        p_data = metrics[p_num]
        if p_data["moves_count"] > 0:
            avg_time = p_data["total_time"] / p_data["moves_count"]
            print(f"\n[Player {p_num}] ({p_data['obj'].__class__.__name__})")
            print(f"  Total Moves Made:       {p_data['moves_count']}")
            print(f"  Total Thinking Time:    {p_data['total_time']:.4f} seconds")
            print(f"  Average Time Per Move:  {avg_time:.4f} seconds")
            print(f"  Max Time Move:          {p_data['max_time']:.6f} seconds")
            # Safe check: if it's our MiniMaxAI, pull the internal state count out
            if hasattr(p_data["obj"], "total_states_explored"):
                print(f"  Total States Explored:  {p_data['obj'].total_states_explored}")
    print("=============================================\n")