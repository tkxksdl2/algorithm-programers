def solution(lst, m, res, ret):
    for i in range(len(lst)-m+1):
        res += [lst[i]]
        if m == 1:
            ret.append(res.copy())
        else:    
            solution(lst[i+1:], m-1, res, ret)
        res.pop()

    return ret

n, m = list(map(int , input().split()))
lst = [str(i) for i in range(1,n+1)]
ret = solution(lst, m, [], [])
for per in ret:
    print(' '.join(per))