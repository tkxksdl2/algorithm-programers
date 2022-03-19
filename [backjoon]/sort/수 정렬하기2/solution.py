import sys
def merge(lst, s, e):
    m = (s + e) // 2
    if e - s <= 1:
        con(lst, s,m,e)
        return 

    merge(lst, s, m)
    merge(lst, m, e)
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
    

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]

merge(lst,0, len(lst))
for i in lst:
    print(i)