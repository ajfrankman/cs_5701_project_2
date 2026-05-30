import argparse
from game_loop import play_game
from players import human_player, ai_random_player

def main():
    parser = argparse.ArgumentParser(description="Play Connect Four with various configurations.")

    parser.add_argument('-r', '--rows', type=int, default=6,
                        help="Number of rows on the board (default: 6)")
    parser.add_argument('-c', '--cols', type=int, default=7,
                        help="Number of columns on the board (default: 7)")
    parser.add_argument('-p1', '--player1', type=str, default="bot", choices=["human", "bot"],
                        help="Type of player for Player 1 (default: bot)")
    parser.add_argument('-p2', '--player2', type=str, default="bot", choices=["human", "bot"],
                        help="Type of player for Player 2 (default: bot)")

    args = parser.parse_args()

    player_types = {
        "human": human_player,
        "bot": ai_random_player
    }
    player_one_func = player_types[args.player1]
    player_two_func = player_types[args.player2]
    
    if (args.rows >= 4 or args.cols >= 4) and args.cols * args.rows >= 8:
        print(f"Starting Connect Four with {args.rows} rows and {args.cols} columns.")
    else:
        print('Seems like a waste of time. but whatever.')
    print(f"Player 1: {args.player1.capitalize()}, Player 2: {args.player2.capitalize()}")

    play_game(player_one_func, player_two_func, rows=args.rows, cols=args.cols)

if __name__ == "__main__":
    main()
