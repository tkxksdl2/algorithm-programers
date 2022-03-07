import heapq
def solution(stones, k):
    section = stones[:3]
    section = set(section)
    print(max(section))
    print(section)
    return


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
print(solution(stones, k))