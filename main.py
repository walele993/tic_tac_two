import random

def initialize_grid():
    """Initialize the grid dictionary with empty spaces."""
    return {pos: " " for pos in ['a1', 'a2', 'a3',
                                 'b1', 'b2', 'b3',
                                 'c1', 'c2', 'c3']}

def initialize_recent_moves():
    """Initialize the dictionary to track recent moves for each player."""
    return {"X": [], "O": []}

def print_grid(grid):
    print("\n")
    print(f" {grid['a1']} | {grid['a2']} | {grid['a3']} ")
    print("-----------")
    print(f" {grid['b1']} | {grid['b2']} | {grid['b3']} ")
    print("-----------")
    print(f" {grid['c1']} | {grid['c2']} | {grid['c3']} ")
    print("\n")

def check_winner(grid, player):
    winning_combinations = [
        ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
        ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
        ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
    ]
    for combo in winning_combinations:
        if grid[combo[0]] == grid[combo[1]] == grid[combo[2]] == player:
            return True
    return False

def is_grid_full(grid):
    return all(cell != " " for cell in grid.values())

def update_grid_with_move(grid, move, player, recent_moves):
    """Update the grid with the player's move and enforce the Last 3 Moves rule."""
    grid[move] = player
    recent_moves.append(move)
    # If more than 3 moves have been made, remove the oldest one
    if len(recent_moves) > 3:
        old_move = recent_moves.pop(0)
        grid[old_move] = " "

def player_turn(grid, player, recent_moves):
    """
    Handle the player's turn.
    Returns the chosen move or "quit" if the player decides to exit.
    """
    while True:
        move = input(f"It's {player}'s turn. Choose a cell (e.g., a1, b2, c3) or type 'quit' to exit: ").strip().lower()
        if move == "quit":
            return "quit"
        if move not in grid:
            print("Invalid cell. Please choose a valid cell (a1, a2, a3, b1, b2, b3, c1, c2, c3).")
            continue
        if grid[move] != " ":
            print("Cell is already occupied. Choose another cell.")
            continue
        break

    update_grid_with_move(grid, move, player, recent_moves)
    return move

def bot_turn(grid, recent_moves):
    """
    The bot uses a simple strategy:
      1. If it can win with a move, it plays that move.
      2. If the opponent can win on the next turn, it blocks that move.
      3. Otherwise, it chooses the center if available, or a random move.
    """
    available = [pos for pos, value in grid.items() if value == " "]
    if not available:
        return None

    # 1. Check for a winning move
    for move in available:
        temp_grid = grid.copy()
        temp_grid[move] = "O"
        if check_winner(temp_grid, "O"):
            print(f"Bot chooses {move} (winning move)")
            update_grid_with_move(grid, move, "O", recent_moves)
            return move

    # 2. Block opponent's winning move
    for move in available:
        temp_grid = grid.copy()
        temp_grid[move] = "X"
        if check_winner(temp_grid, "X"):
            print(f"Bot chooses {move} (blocking move)")
            update_grid_with_move(grid, move, "O", recent_moves)
            return move

    # 3. Choose the center if available
    if grid['b2'] == " ":
        print("Bot chooses b2 (center)")
        update_grid_with_move(grid, 'b2', "O", recent_moves)
        return 'b2'

    # 4. Otherwise, choose a random move
    move = random.choice(available)
    print(f"Bot chooses {move} (random move)")
    update_grid_with_move(grid, move, "O", recent_moves)
    return move

def play_two_player():
    grid = initialize_grid()
    recent_moves = initialize_recent_moves()
    current_player = "X"

    while True:
        print_grid(grid)
        move = player_turn(grid, current_player, recent_moves[current_player])
        if move == "quit":
            print("Game terminated.")
            break

        if check_winner(grid, current_player):
            print_grid(grid)
            print(f"Player {current_player} wins!")
            break

        if is_grid_full(grid):
            print_grid(grid)
            print("It's a draw!")
            break

        # Switch turn to the other player
        current_player = "O" if current_player == "X" else "X"

def play_vs_bot():
    grid = initialize_grid()
    recent_moves = initialize_recent_moves()
    # The user plays as "X" and the bot as "O"
    current_player = "X"

    while True:
        print_grid(grid)
        if current_player == "X":
            move = player_turn(grid, "X", recent_moves["X"])
            if move == "quit":
                print("Game terminated.")
                break
            if check_winner(grid, "X"):
                print_grid(grid)
                print("You win!")
                break
            current_player = "O"
        else:
            print("Bot's turn.")
            bot_turn(grid, recent_moves["O"])
            if check_winner(grid, "O"):
                print_grid(grid)
                print("Bot wins!")
                break
            current_player = "X"

        if is_grid_full(grid):
            print_grid(grid)
            print("It's a draw!")
            break

def main():
    print("Welcome to Tic Tac Toe with Last 3 Moves Rule!")
    while True:
        mode = input("Choose game mode: 1 for Two Players, 2 for Play vs Bot (or type 'quit' to exit): ").strip().lower()
        if mode == "quit":
            print("Goodbye!")
            break
        elif mode == "1":
            play_two_player()
        elif mode == "2":
            play_vs_bot()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
