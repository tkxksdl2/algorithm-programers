def solution(lst, m, res, ret, used=set()):
    for i in range(len(lst)):
        if lst[i] not in used:
            res += [lst[i]]
            used.add(lst[i])
            if m == 1:
                ret.append(res.copy())
            else:    
                solution(lst, m-1, res, ret)
            res.pop()
            used.remove(lst[i])

    return ret

n, m = list(map(int , input().split()))
lst = [str(i) for i in range(1,n+1)]
ret = solution(lst, m, [], [])
for per in ret:
    print(' '.join(per))