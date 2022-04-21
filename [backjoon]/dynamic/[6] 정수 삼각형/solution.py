def solution(tri):
    for i in range(1, len(tri)):
        for j, v in enumerate(tri[i]):
            if j == 0:
                tri[i][j] = tri[i-1][j] + v
            elif j == len(tri[i]) - 1:
                tri[i][j] = tri[i-1][j-1] + v
            else:
                tri[i][j] = v + max(tri[i-1][j-1], tri[i-1][j])            
    
    return max(tri[n-1])

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

print((solution(tri)))