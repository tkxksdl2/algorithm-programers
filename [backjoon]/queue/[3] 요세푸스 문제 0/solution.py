n, k = map(int, input().split())

lst = [i for i in range(n + 1)]
p = 1
ans = []
while p < len(lst):
    if p % k != 0:
        lst.append(lst[p])
    else: ans.append(lst[p])

    p += 1

print('<' + ', '.join(list(map(str, ans))) + '>')