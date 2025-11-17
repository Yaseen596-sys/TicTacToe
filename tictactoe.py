"""
Tic-Tac-Toe project.

Step 5:
- Add replay option.
- Track scores for X, O, and draws across multiple games.
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
    """Check the board for a winner or a draw."""
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
    """Play one complete game and return the result: 'X', 'O', or 'draw'."""
    board = create_board()
    current_player = PLAYER_X
    result = None

    print("\nNew game started! Player X goes first.")

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

    return result


def main():
    """Main loop to play multiple games and track scores."""
    print("Welcome to Tic-Tac-Toe!")
    scores = {PLAYER_X: 0, PLAYER_O: 0, "draw": 0}

    while True:
        result = play_single_game()
        if result in scores:
            scores[result] += 1

        print("\nCurrent scores:")
        print(f"  Player X: {scores[PLAYER_X]}")
        print(f"  Player O: {scores[PLAYER_O]}")
        print(f"  Draws   : {scores['draw']}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
