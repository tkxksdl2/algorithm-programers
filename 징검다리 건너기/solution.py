from collections import deque

def solution(stones, k):
    section = deque(stones[:k])
    max_idx =0

    for i in range(1, len(section)):
        if section[i] >= section[max_idx]: max_idx = i
    answer = section[max_idx]

    for i in range(k, len(stones)):
        if stones[i] >= section[max_idx]:
            max_idx = k
        section.popleft()
        section.append(stones[i])
        
        if max_idx == 0:
            for i in range(1, len(section)):
                if section[i] >= section[max_idx]: max_idx = i
        else:
            max_idx -= 1
        answer = min(answer, section[max_idx])

    return answer
 

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
print(solution(stones, k))