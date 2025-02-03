# Tic Tac Two

**Work in Progress**

Tic Tac Two is an innovative twist on the classic Tic Tac Toe game, implemented in Python. In this version, players are allowed to keep only their last three moves on the board, making the game longer and more strategic. The game supports both two-player mode and play against a bot with a basic strategy. Future enhancements include a graphical user interface and user account creation with game history tracking.

## Features

- **Last 3 Moves Rule:** Each player’s earlier moves are removed once they make a fourth move, keeping the board dynamic.
- **Multiple Game Modes:**
  - **Two-Player Mode:** Play against another human.
  - **Play vs Bot Mode:** Challenge a bot that uses a simple strategy to win or block your moves.
- **User Input Handling:** Players can type `quit` at any time to exit the game.
- **Console-Based Gameplay:** The board is displayed in a text format, ensuring the game runs in any terminal.

## Project Structure

The project is organized into a single main script for simplicity, with clear sections handling different aspects of the game:

- **Grid Management:** Functions to initialize, print, and update the grid.
- **Game Logic:** Functions to check for a winner, determine if the grid is full, and enforce the Last 3 Moves rule.
- **Player and Bot Turns:** Functions to handle user input and implement the bot’s strategy (winning move, blocking move, center preference, or random move).
- **Game Modes:** Separate functions to manage the two-player game mode and play vs bot mode.
- **Main Loop:** The main entry point of the program which allows the user to choose the game mode or exit.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/tic_tac_two_the_game.git
   cd tic_tac_two_the_game
   
1. **Run the game:**

   ```bash
   python main.py

## Future Goals

- **Graphical User Interface:** Develop a full-featured GUI (using Tkinter, PyQt, or another framework) to enhance the user experience.
- **User Accounts and History:** Implement account creation and tracking so players can view their game history and statistics.
- **Enhanced Bot Intelligence:** Further refine the bot’s strategy for a more challenging single-player experience.
- **Additional Features:** Incorporate animations, sound effects, and online multiplayer capabilities.

## Feedback and Contributions

Your feedback, suggestions, and contributions are welcome! If you encounter any issues or have ideas for improvements, please feel free to open an issue or submit a pull request on GitHub.

## Credits

This project was created by Gabriele Meucci.

---

*Happy coding and enjoy the game!*
