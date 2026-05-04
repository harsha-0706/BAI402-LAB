def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    return True


def solve(board, row):
    n = len(board)
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row+1):
                return True
            board[row][col] = 0
    return False


n = 8
board = [[0]*n for _ in range(n)]

if solve(board, 0):
    for r in board:
        print(r)
else:
    print("No solution")
