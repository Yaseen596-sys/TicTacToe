"""
Simple terminal-based Tic-Tac-Toe game.

Features:
- Two-player game (X and O).
- Input validation (only accepts free positions 1–9).
- Replay option without restarting the program.
- Score tracking across multiple rounds.
"""

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "


def create_board():
    """Create and return a new empty 3x3 Tic-Tac-Toe board."""
    return [EMPTY] * 9


def print_board(board):
    """
    Print the current board in a 3x3 layout.

    Empty cells show their position number (1–9) so players know
    what to type for their move.
    """
    display = []
    for i, cell in enumerate(board):
        if cell == EMPTY:
            display.append(str(i + 1))
        else:
            display.append(cell)

    print()
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print()


def get_player_move(board, current_player):
    """
    Ask current player for a valid move (1–9, not occupied).

    Returns:
        int: index on the board (0–8).
    """
    while True:
        choice = input(f"Player {current_player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        pos = int(choice)
        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9.")
            continue

        index = pos - 1
        if board[index] != EMPTY:
            print("That position is already taken. Please choose another.")
            continue

        return index


def check_winner(board):
    """
    Check the board for a winner or a draw.

    Returns:
        "X" if player X wins,
        "O" if player O wins,
        "draw" if no spaces left and no winner,
        None if the game should continue.
    """
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_combinations:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]

    if EMPTY not in board:
        return "draw"

    return None


def play_single_game():
    """
    Play one complete game of Tic-Tac-Toe.

    Returns:
        str: "X", "O", or "draw" based on the result.
    """
    board = create_board()
    current_player = PLAYER_X
    result = None

    print("\nNew game started!")
    print("Player X goes first.")
    print("Enter a number (1-9) to place your mark in that position.")
    print_board(board)

    while result is None:
        index = get_player_move(board, current_player)
        board[index] = current_player
        print_board(board)
        result = check_winner(board)
        if result is None:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    if result == "draw":
        print("It's a draw!")
    else:
        print(f"Player {result} wins!")

    return result


def ask_play_again():
    """Ask the players if they want to play again. Return True if yes, else False."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def main():
    """
    Main loop for the Tic-Tac-Toe project.

    Keeps playing games until users choose to stop,
    and tracks total scores for both players and draws.
    """
    print("Welcome to Tic-Tac-Toe!")
    print("Two players take turns placing X and O on a 3x3 board.\n")

    scores = {PLAYER_X: 0, PLAYER_O: 0, "draw": 0}

    while True:
        result = play_single_game()
        if result in scores:
            scores[result] += 1

        print("\nCurrent scores:")
        print(f"  Player X: {scores[PLAYER_X]}")
        print(f"  Player O: {scores[PLAYER_O]}")
        print(f"  Draws   : {scores['draw']}\n")

        if not ask_play_again():
            print("Thanks for playing Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
