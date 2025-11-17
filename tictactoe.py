"""
Tic-Tac-Toe project.

Step 2:
- Add basic board representation.
- Add print_board function to show the board.
"""

EMPTY = " "


def create_board():
    """Create and return a new empty 3x3 Tic-Tac-Toe board."""
    return [EMPTY] * 9  # 9 positions: indices 0–8


def print_board(board):
    """Print the current board in a user-friendly 3x3 layout."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def main():
    """Entry point for the Tic-Tac-Toe program."""
    print("Welcome to Tic-Tac-Toe!")
    board = create_board()
    print("Empty board:")
    print_board(board)


if __name__ == "__main__":
    main()
