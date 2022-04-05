def sudoku(board):
    # [i][j] 일 때 i 번째 행, 열, 박스에 j 라는 숫자가 존재하는지 여부
    checkrow = [[False for _ in range(9)] for _ in range(9)]
    checkcol = [[False for _ in range(9)] for _ in range(9)]
    checkbox = [[False for _ in range(9)] for _ in range(9)]

    # 고정된 숫자 입력
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0: continue
            checkrow[y][board[y][x]-1] = checkcol[x][board[y][x]-1] = True
            checkbox[calbox(x,y)][board[y][x]-1] = True

    dfs(board, 0, checkrow, checkcol, checkbox )
    return

def dfs(board, n, checkrow, checkcol, checkbox):
    # 끝까지 dfs 완료된 경우 결과 출력.
    # 모든 자리의 return이 True이어야만 여기까지 도착하고 함수를 끝낼 수 있다.
    if n == 81:
        for row in board:
            for v in row:
                print(v, end=' ')
            print()
        return True

    y = n // 9
    x = n % 9
    # 이미 입력된 자리일 경우 다음 자리로 넘어감
    if board[y][x] != 0:
        return dfs(board, n + 1, checkrow, checkcol, checkbox)
    # 빈 칸일경우 1~9까지 시도
    for i in range(9):
        # 숫자가 각 행, 열, 박스에 이미 있는지 검증
        if not checkrow[y][i] and not checkcol[x][i] and not checkbox[calbox(x,y)][i]:
            checkrow[y][i] = checkcol[x][i] = checkbox[calbox(x,y)][i] = True
            board[y][x] = i + 1

            # 숫자가 없다면 그 숫자를 넣고 다음 자리로 넘어감.
            if dfs(board, n + 1, checkrow, checkcol, checkbox):
                return True
            # 다음 자리에서 모든 경우의 수가 조건을 만족하지 못했다면 여기로 돌아온다.
            # 이 자리의 이 숫자의 모든 분기가 실패했으므로 넣었던 숫자를 취소하고 다음 숫자를 확인.
            checkrow[y][i] = checkcol[x][i] = checkbox[calbox(x,y)][i] = False
            board[y][x] = 0
    
    # 이 자리에서 모든 숫자가 조건을 만족하지 못했다.
    # 따라서 False를 리턴하고 이전 분기로 돌아간다.
    return False

def calbox(x,y):
    return (y//3)*3 + x//3

# board = [ list(map(int, input().split())) for _ in range(9)]
board = [[0, 3, 5, 4, 6, 9, 0, 7, 8],
        [7, 8, 2, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 2, 7, 8, 1, 3, 5],
        [3, 2, 1, 0, 4, 6, 8, 9, 7],
        [8, 0, 4, 9, 1, 3, 5, 0, 6],
        [5, 9, 6, 8, 2, 0, 4, 1, 3],
        [9, 1, 7, 6, 5, 2, 0, 8, 0],
        [6, 0, 3, 7, 0, 1, 9, 5, 2],
        [2, 5, 8, 3, 9, 4, 7, 6, 0]]
sudoku(board)