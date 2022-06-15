def solution(n, roads, costs):
    c = costs[0]
    ans = c * roads[0]
    for i in range(1, n-1):
        if costs[i] < c:
            c = costs[i]
        ans += c * roads[i]
    
    print(ans)

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
solution(n, roads, costs)