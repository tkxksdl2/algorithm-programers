def solution(n):
    v1, v2 = 1, 2
    ret = 0

    if n == 0: return ret
    elif n == 1: return v1
    elif n == 2: return v2

    for i in range(3, n+1):
        ret = (v1 + v2) % 15746
        v1 = v2; v2 = ret
        
    return ret % 15746


n = int(input())
print(solution(n))