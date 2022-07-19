def solution(stones, k):
    s = min(stones)
    e = max(stones)

    while s < e:
        mid = (s+e) // 2 + 1
        cnt = 0

        for n in stones:
            if n < mid: cnt += 1
            else: cnt = 0
            if cnt == k: break
        
        if cnt == k: e = mid-1
        else: s = mid
    
    return s

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
print(solution(stones, k))