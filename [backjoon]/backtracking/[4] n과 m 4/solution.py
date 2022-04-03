def solution(lst, m, res):
    for i in range(len(lst)):
        res += [lst[i]]
        if m == 1:
            print(' '.join(res))
        else:
            solution(lst[i:], m-1, res)
        res.pop()


n, m = list(map(int , input().split()))
lst = [str(i) for i in range(1,n+1)]
ret = solution(lst, m, [])