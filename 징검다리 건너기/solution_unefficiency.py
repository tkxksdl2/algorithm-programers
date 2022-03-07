def solution(stones, k):
    answer = float('inf')

    for i in range(len(stones)-k+1):
        section = stones[i:i+k]
        answer = min(answer, max(section))

    return answer
 

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
print(solution(stones, k))