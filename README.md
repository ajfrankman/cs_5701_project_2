# Connect Four Game

This project implements a classic Connect Four game in Python. It features a command-line interface for playing, with options for human players and a basic random AI. The architecture is designed to allow for easy integration of more advanced AI algorithms in the future.

## Features

*   **Human vs. AI**: Play against an AI
*   **Game Logic**: Implements all core Connect Four rules, including piece dropping, win condition checking (horizontal, vertical, and diagonal), and draw detection.
*   **Modular Design**: Player logic is separated, allowing for easy expansion with new AI strategies.
*   **Rich Console Output**: Uses the `rich` library for an enhanced terminal display of the game board.

## Getting Started

### Prerequisites

To run this game, you need Python 3.6+ and the `numpy` and `rich` libraries.
You can install these dependencies using pip:

```bash
pip install numpy richß
```

### How to Run

To start a game with the default settings (6x7 board, two bot players), execute `main.py`:

```bash
python main.py
```

You can also customize the game by providing command-line arguments:

*   `--rows <int>`: Number of rows on the board (default: 6)
*   `--cols <int>`: Number of columns on the board (default: 7)
*   `--player1 {human,bot}`: Type of player for Player 1 (default: bot)
*   `--player2 {human,bot}`: Type of player for Player 2 (default: bot)

**Examples:**

*   **Human vs. Bot on a 7x6 board:**
    ```bash
    python main.py --player1 human --player2 bot
    ```

*   **Two Human Players on an 8x8 board:**
    ```bash
    python main.py --rows 8 --cols 8 --player1 human --player2 human
    ```

*   **Two Bots on a default 6x7 board:**
    ```bash
    python main.py --player1 bot --player2 bot
    ```

Follow the prompts in the console to make your moves if playing as a human.

## Project Structure

*   `board_utils.py`: Contains the `Board` class, which manages the game board state, piece placement, win condition checks, and board visualization.
*   `players.py`: Defines various player functions, including `human_player` for human input and `ai_random_player` for a basic AI opponent.
*   `game_loop.py`: Orchestrates the main game flow, handling turns, applying moves, and checking for game-ending conditions.
*   `scratch.py`: An entry point to quickly start a game, currently configured for a human versus the random AI.

## Future Enhancements

The project is set up to easily integrate more sophisticated AI algorithms. Future plans include implementing various search algorithms (e.g., Minimax, Alpha-Beta Pruning) to create more challenging AI opponents.
