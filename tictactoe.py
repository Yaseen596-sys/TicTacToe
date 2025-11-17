"""
Tic-Tac-Toe project.

Step 3:
- Allow two players to place X and O on the board.
- Simple input validation for position.
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
    """
    Ask current player for a move.
    Very basic validation: must be 1–9 and empty.
    """
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


def main():
    """Entry point for the Tic-Tac-Toe program."""
    print("Welcome to Tic-Tac-Toe!")
    board = create_board()
    current_player = PLAYER_X

    # Let players make a few moves (not full game yet)
    for _ in range(5):
        print_board(board)
        index = get_player_move(board, current_player)
        board[index] = current_player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    print_board(board)
    print("Demo complete – full game logic will be added later.")


if __name__ == "__main__":
    main()
