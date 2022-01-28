def solution(m, n, board):
    board = [list(row) for row in board]
    while True:
        del_idx = []
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] != 0 and board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                    del_idx.append([row,col])

        if not del_idx:
            break

        for row, col in del_idx:
            board[row][col] = board[row+1][col] = board[row][col+1] = board[row+1][col+1] = 0

        for row in range(1, m):
            for col in range(n):
                if board[row][col] == 0:
                    for r in range(row, 0, -1):
                        board[r][col] = board[r-1][col]
                        board[r-1][col] = 0

    return sum([row.count(0) for row in board])
m, n = 6,6
board =["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m,n,board))