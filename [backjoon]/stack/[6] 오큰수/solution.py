import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

idxs = [-1 for _ in range(n)]
max = 0
ans = []

for i in range(n-1, -1, -1):
    num = lst[i]
    if lst[i] >= max:
        ans.append(-1)
        max = num
    else:
        j = i+1
        while True:
            if lst[j] <= num:
                j = idxs[j]
            else:
                idxs[i] = j; ans.append(lst[j])
                break
    
for i in ans[::-1]:
    print(i, end=' ')

