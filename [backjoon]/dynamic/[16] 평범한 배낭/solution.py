def solution(n, b, items):
    cache = [[0 for _ in range(b+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, b+1):
            if items[i-1][0] <=j:
                cache[i][j] = max(cache[i-1][j], cache[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                cache[i][j] = cache[i-1][j]

    print(cache[n][b])

n, b = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
solution(n, b, items)
