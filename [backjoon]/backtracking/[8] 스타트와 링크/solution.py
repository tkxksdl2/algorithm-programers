from itertools import combinations as c

def solution(n, info):
    allmem = [i for i in range(n)]
    combs = c(allmem, n//2)
    minval = float('inf')
    for s_team in combs:
        l_team = [i for i in range(n) if i not in s_team]

        s_score = l_score = 0
        for y,x in c(s_team, 2):
            s_score += info[y][x] + info[x][y]
        for y,x in c(l_team, 2):
            l_score += info[y][x] + info[x][y]
        
        f_score = abs(s_score - l_score)
        if f_score < minval: minval = f_score

    print(minval)


n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
solution(n, info)
