"""
Tic-Tac-Toe project.

Step 4:
- Add winner and draw detection.
- Play until someone wins or the board is full.
"""

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "


def create_board():
    """Create and return a new empty 3x3 Tic-Tac-Toe board."""
    return [EMPTY] * 9


def print_board(board):
    """Print the current board in a user-friendly 3x3 layout."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def get_player_move(board, current_player):
    """Ask current player for a valid move (1–9, not occupied)."""
    while True:
        choice = input(f"Player {current_player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        pos = int(choice)
        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9.")
            continue

        index = pos - 1
        if board[index] != EMPTY:
            print("That position is already taken.")
            continue

        return index


def check_winner(board):
    """
    Check the board for a winner or a draw.
    Returns "X", "O", "draw", or None.
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


def main():
    """Run a single game of Tic-Tac-Toe."""
    print("Welcome to Tic-Tac-Toe!")
    board = create_board()
    current_player = PLAYER_X
    result = None

    while result is None:
        print_board(board)
        index = get_player_move(board, current_player)
        board[index] = current_player
        result = check_winner(board)
        if result is None:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    print_board(board)
    if result == "draw":
        print("It's a draw!")
    else:
        print(f"Player {result} wins!")


if __name__ == "__main__":
    main()
