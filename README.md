# Connect Four Game

This project implements a classic Connect Four game in Python. It features a command-line interface for playing, with options for human players and a basic random AI. The architecture is designed to allow for easy integration of more advanced AI algorithms in the future.

## Features

*   **Human vs. AI**: Play against a simple AI that makes random valid moves.
*   **Game Logic**: Implements all core Connect Four rules, including piece dropping, win condition checking (horizontal, vertical, and diagonal), and draw detection.
*   **Modular Design**: Player logic is separated, allowing for easy expansion with new AI strategies.
*   **Rich Console Output**: Uses the `rich` library for an enhanced terminal display of the game board.

## Getting Started

### Prerequisites

To run this game, you need Python 3.6+ and the `numpy` and `rich` libraries.
You can install these dependencies using pip:

```bash
pip install numpy rich
```

### How to Run

To start a game with a human player against the random AI, execute the `scratch.py` file:

```bash
python scratch.py
```

Follow the prompts in the console to make your moves.

## Project Structure

*   `board_utils.py`: Contains the `Board` class, which manages the game board state, piece placement, win condition checks, and board visualization.
*   `players.py`: Defines various player functions, including `human_player` for human input and `ai_random_player` for a basic AI opponent.
*   `game_loop.py`: Orchestrates the main game flow, handling turns, applying moves, and checking for game-ending conditions.
*   `scratch.py`: An entry point to quickly start a game, currently configured for a human versus the random AI.

## Future Enhancements

The project is set up to easily integrate more sophisticated AI algorithms. Future plans include implementing various search algorithms (e.g., Minimax, Alpha-Beta Pruning) to create more challenging AI opponents.
