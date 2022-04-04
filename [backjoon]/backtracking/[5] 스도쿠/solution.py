def sudoku(board):
    unknown = []
    blank = [[] for _ in range(9)]
    for y, row in enumerate(board):
        known = set(i for i in range(1,10))
        for x, v in enumerate(row):
            if v == 0: 
                blank[y].append([y,x])
                continue
            known.remove(v)
        
        unknown.append(list(known))

    unknown_perm = [ permutation(lst, len(lst), [], []) for lst in unknown]
    perm_idx = [len(unknown_perm[i])-1 for i in range(9)]

    while True:
        ## 할
        for y, b in enumerate(blank):
            for c, idx in enumerate(b):
                board[idx[0]][idx[1]] = unknown_perm[y][perm_idx[y]][c]
        ## 검사
        isfaild = False
        # 가로 세로
        for i in range(9):
            checkrow, checkcol = set(), set()
            for j in range(9):
                if board[i][j] in checkrow or board[j][i] in checkcol:
                    isfaild = True; break
                checkrow.add(board[i][j])
                checkcol.add(board[j][i])
            if isfaild: break
        # 박스
        if not isfaild:
            sy, sx = 0, 0
            while True:
                checkbox = set()
                for dy in range(3):
                    for dx in range(3):
                        if board[sy+dy][sx+dx] in checkbox:
                            isfaild = True; break
                        checkbox.add(board[sy+dy][sx+dx])
                if isfaild: break

                if sy>= 6 and sx>=6: break
                elif sy >= 6:
                    sy = 0; sx += 3
                else:
                    sy += 3 

        if not isfaild:
            for row in board:
                for v in row:
                    print(v, end=' ')
                print()
            break
        # 다음 루트
        for i in range(len(perm_idx)):
            if perm_idx[i] == 0: continue
            perm_idx[i] -= 1
            for j in range(i):
                perm_idx[j] = len(unknown_perm[j]) - 1
            break
    return

def permutation(lst, m, res=[], ret=[], dup=set()):
    for v in lst:
        if v in dup: continue
        res += [v]
        dup.add(v)
        if m == 1:
            ret.append(res.copy())
        else:
            permutation(lst, m-1, res, ret, dup)
        
        res.pop(); dup.remove(v)
    
    return ret

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