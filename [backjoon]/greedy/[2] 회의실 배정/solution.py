import sys
def solution(n, lst):
    lst.sort(key= lambda x:[x[1], x[0]])

    cnt = 0; endtime = 0
    for s, e in lst:
        if s >= endtime:
            cnt += 1; endtime = e
    
    print(cnt)

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
solution(n, lst)