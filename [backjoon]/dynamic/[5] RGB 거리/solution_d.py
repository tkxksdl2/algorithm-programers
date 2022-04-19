def solution(cost, n):
    for i in range(1, n):
        for j in range(3):
            cost[i][j] = cost[i][j] + min(cost[i-1][(j-1)%3], cost[i-1][(j+1)%3])

    return min(cost[n-1])


n = int(input())
cost =  [list(map(int, input().split())) for _ in range(n)]

print(solution(cost, n))