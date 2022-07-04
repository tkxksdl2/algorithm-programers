import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    sorted_lst = sorted(lst, key= lambda x: -x)
    f, max_i = 0, 0
    cnt = 0

    while f < len(lst):
        if lst[f] == sorted_lst[max_i]:
            if f == m:
                print(cnt+1)
                break
            else:
                cnt += 1
                max_i += 1
        else:
            lst.append(lst[f])
            if f == m:
                m = len(lst) - 1
        f += 1



