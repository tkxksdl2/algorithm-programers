import sys

def solution(n):
    lst = [[] for _ in range(50)]
    res = []
    dup = set()

    for _ in range(n):
        w = sys.stdin.readline().strip()
        if w in dup: continue
        else:
            lst[len(w)-1] += [w]
            dup.add(w)
    
    for row in lst:
        res += sorted(row)

    for w in res:
        print(w)


n = int(sys.stdin.readline())
solution(n)
