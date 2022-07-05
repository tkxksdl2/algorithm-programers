n, m = map(int, input().split())
obs = list(map(int, input().split()))
lst = [i+1 for i in range(n)]
s = 0; cnt = 0

for i in range(m):
    ob = obs[i]
    l, r = 0, 0
    while True:
        li = (s - l) % len(lst)
        ri = (s + r) % len(lst)
        if lst[li] == ob:
            lst.pop(li); cnt += l
            s = li % len(lst) if lst else None #빈 리스트 예외처리 n == m
            break
        elif lst[ri] == ob:
            lst.pop(ri); cnt += r
            s = ri % len(lst) if lst else None
            break
        
        l += 1; r += 1
        
print(cnt)