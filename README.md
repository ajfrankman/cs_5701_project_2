# Connect Four Game

This project implements a classic Connect Four game in Python. It features a command-line interface for playing, with options for human players and AI opponents including a Minimax AI with alpha-beta pruning.

## Features

*   **Multiple Player Types**: Human, Random AI, and Minimax AI with configurable search depth
*   **Game Logic**: Implements all core Connect Four rules, including piece dropping, win condition checking (horizontal, vertical, and diagonal), and draw detection
*   **Minimax AI with Alpha-Beta Pruning**: Strategic AI opponent that can be tuned for difficulty via search depth
*   **Performance Metrics**: Tracks thinking time, move counts, and states explored for AI players
*   **Rich Console Output**: Uses the `rich` library for an enhanced terminal display of the game board

## Getting Started

### Prerequisites

To run this game, you need Python 3.6+ and the `numpy` and `rich` libraries.
You can install these dependencies using pip:

```bash
pip install numpy rich
```

### How to Run

To start a game with the default settings (6x7 board, human vs minimax AI), execute `main.py`:

```bash
python main.py
```

You can customize the game by providing command-line arguments:

*   `-r, --rows <int>`: Number of rows on the board (default: 6)
*   `-c, --cols <int>`: Number of columns on the board (default: 7)
*   `-p1, --player1 {human,random_bot,minimax_bot}`: Type of player for Player 1 (default: human)
*   `-p2, --player2 {human,random_bot,minimax_bot}`: Type of player for Player 2 (default: minimax_bot)
*   `-d1, --depth1 <int>`: Search depth for Player 1's AI (default: 3)
*   `-d2, --depth2 <int>`: Search depth for Player 2's AI (default: 3)

**Examples:**

*   **Human vs. Random Bot on default 6x7 board:**
    ```bash
    python main.py --player1 human --player2 random_bot
    ```

*   **Two Humans on default 6x7 board:**
    ```bash
    python main.py --player1 human --player2 human
    ```

*   **Human vs Minimax Bot with increased depth:**
    ```bash
    python main.py --player2 minimax_bot --depth2 5
    ```

*   **Two Minimax Bots on an 8x8 board:**
    ```bash
    python main.py --rows 8 --cols 8 --player1 minimax_bot --player2 minimax_bot
    ```

Follow the prompts in the console to make your moves if playing as a human.

## Project Structure

*   `main.py`: Entry point with argument parsing and game initialization
*   `board_utils.py`: Contains the `Board` class for managing game state, piece placement, win condition checks, and board visualization
*   `players.py`: Defines player classes including `Human`, `RandomAI`, and `MiniMaxAI` with alpha-beta pruning
*   `game_loop.py`: Orchestrates the main game flow, handling turns, applying moves, and displaying performance metrics
*   `scratch.py`: Quick entry point for testing specific configurations

## AI Implementation

The `MiniMaxAI` uses the Minimax algorithm with alpha-beta pruning for efficient state evaluation. It includes:
- Configurable search depth to control difficulty
- Heuristic evaluation using an optimal position matrix
- Depth-weighted scoring to prefer faster wins and delayed losses
- Performance tracking of total states explored

## Future Enhancements

Possible future improvements include:
- Transposition Table