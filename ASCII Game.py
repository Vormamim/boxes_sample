def create_board():
    board = [[' ' for _ in range(9)] for _ in range(9)]
    return board

def print_board(board):
    print("   " + " ".join(str(i) for i in range(9)))
    for i in range(9):
        print(f"{i}  " + " ".join(board[i]))
    print()

def check_win(board, player, row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        x, y = row + dx, col + dy
        while 0 <= x < 9 and 0 <= y < 9 and board[x][y] == player:
            count += 1
            x, y = x + dx, y + dy
        x, y = row - dx, col - dy
        while 0 <= x < 9 and 0 <= y < 9 and board[x][y] == player:
            count += 1
            x, y = x - dx, y - dy
        if count >= 5:
            return True
    return False

def make_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0-8): "))
            col = int(input(f"Player {player}, enter the column (0-8): "))
            if 0 <= row < 9 and 0 <= col < 9 and board[row][col] == ' ':
                board[row][col] = player
                return row, col
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Try again.")

def play_gomoku():
    board = create_board()
    current_player = "X"

    print("Welcome to Gomoku (ASCII version)!")
    print("Player X starts. Players take turns entering row and column coordinates to make their moves.")

    for turn in range(9 * 9): 
        print_board(board)
        row, col = make_move(board, current_player)

        if check_win(board, current_player, row, col):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    play_gomoku()
