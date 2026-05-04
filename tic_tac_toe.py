def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)


def check_winner(board, p):
    for row in board:
        if all(c == p for c in row):
            return True
    for col in range(3):
        if all(board[r][col] == p for r in range(3)):
            return True
    if all(board[i][i] == p for i in range(3)) or all(board[i][2-i] == p for i in range(3)):
        return True
    return False


def full(board):
    return all(c != ' ' for r in board for c in r)


board = [[' ']*3 for _ in range(3)]
player = 'X'

while True:
    print_board(board)
    r = int(input("Row: ")) - 1
    c = int(input("Col: ")) - 1

    if board[r][c] != ' ':
        print("Invalid move")
        continue

    board[r][c] = player

    if check_winner(board, player):
        print_board(board)
        print(player, "wins")
        break

    if full(board):
        print("Draw")
        break

    player = 'O' if player == 'X' else 'X'
