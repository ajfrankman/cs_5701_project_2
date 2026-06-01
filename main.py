import argparse
from game_loop import play_game
from players import Human, RandomAI, MiniMaxAI


def get_players(args):
    player_types = {
        "human": Human,
        "random_bot": RandomAI,
        "minimax_bot": MiniMaxAI
    }
    P1 = player_types[args.player1]
    P2 = player_types[args.player2]
    if 'AI' in str(P1):
        p1 = P1(1, args.depth1)
    else:
        p1 = P1(1)
    if 'AI' in str(P2):
        p2 = P2(2, args.depth2)
    else:
        p2 = P2(2)

    return p1, p2



def main():
    parser = argparse.ArgumentParser(description="Play Connect Four with various configurations.")

    parser.add_argument('-r', '--rows', type=int, default=6,
                        help="Number of rows on the board (default: 6)")
    parser.add_argument('-c', '--cols', type=int, default=7,
                        help="Number of columns on the board (default: 7)")
    parser.add_argument('-p1', '--player1', type=str, default="human", choices=["human", "random_bot", "minimax_bot"],
                        help="Type of player for Player 1 (default: human)")
    parser.add_argument('-p2', '--player2', type=str, default="minimax_bot", choices=["human", "random_bot", "minimax_bot"],
                        help="Type of player for Player 2 (default: minimax_bot)")
    parser.add_argument('-d1', '--depth1', type=int, default=3,
                        help="Depth of search for p1 (default: 3)")
    parser.add_argument('-d2', '--depth2', type=int, default=3,
                        help="Depth of search for p2 (default: 3)")

    args = parser.parse_args()

    player_one, player_two = get_players(args)
    
    if (args.rows >= 4 or args.cols >= 4) and args.cols * args.rows >= 8:
        print(f"Starting Connect Four with {args.rows} rows and {args.cols} columns.")
    else:
        print('Seems like a waste of time. but whatever.')
    print(f"Player 1: {args.player1}, Player 2: {args.player2}")
    print('To see game options, run the program with the "-h" or "--help" flag.')

    play_game(player_one, player_two, rows=args.rows, cols=args.cols)

if __name__ == "__main__":
    main()
