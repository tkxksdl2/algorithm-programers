import sys

def solution(lst, s, e ):
    m = (s+e) // 2
    if e - s <=2:
        merge(lst,s,m,e)
        return
    solution(lst,s,m)
    solution(lst,m,e)

    merge(lst, s, m, e)

    
def merge(lst, s, m, e):
    i, j = s, m
    res = []
    while i < m and j < e:
        if lst[i][0] == lst[j][0]:
            if lst[i][1] <= lst[j][1]:
                res += [lst[i]]
                i += 1
            else:
                res += [lst[j]]
                j += 1
        elif lst[i][0] < lst[j][0]:
            res += [lst[i]]
            i += 1
        else:
            res += [lst[j]]
            j += 1
    
    while i < m: res += [lst[i]]; i+=1
    while j < s: res += [lst[j]]; j+=1

    for v in res:
        lst[s] = v; s+=1

n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


solution(lst, 0, n)
for a,b in lst:
    print(a, b)