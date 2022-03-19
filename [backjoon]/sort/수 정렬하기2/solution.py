import sys
def merge(lst, s, e):
    m = (s + e) // 2
    left = lst[s:m]
    right = lst[m:e]
    if e - s <= 1:
        return con(lst, s,m,e)

    left = merge(lst, s, m)
    right = merge(lst, m, e)
    con(lst, s, m ,e)

def con(lst, s, m, e):
    res = []
    i, j = s, m
    while i < m and j < e:
        if lst[i] <= lst[j]:
            res.append(lst[i])
            i += 1
        else:
            res.append(lst[j])
            j += 1

    while i < m: res.append(lst[i]); i+=1  
    while j < e: res.append(lst[j]); j+=1  
    
    for v in res:
        lst[s] = v
        s += 1
    
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]

merge(lst,0, len(lst))
print(lst)