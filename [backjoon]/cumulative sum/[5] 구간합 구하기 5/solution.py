import sys
def solution(n, m, mat):
    for i in range(1, n):
        mat[i][0] += mat[i-1][0]
        mat[0][i] += mat[0][i-1]
    for i in range(1, n):
        for j in range(1, n):
            mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

    for _ in range(m):
        x1,y1, x2, y2 = map(int, sys.stdin.readline().split())
        a = mat[x2-1][y1-2] if y1 > 1 else 0
        b = mat[x1-2][y2-1] if x1 > 1 else 0
        c = mat[x1-2][y1-2] if x1 > 1 and y1 > 1 else 0
        
        print(mat[x2-1][y2-1] - a - b + c)
    return

n, m = map(int, input().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
solution(n,m,mat)