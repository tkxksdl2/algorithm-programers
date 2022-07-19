def solution(n, s, a, b, fares):
    INF = 200 * 200000 +1
    
    fares_dict = dict()
    for i in range(1, n+1):
        fares_dict[i] = dict()
        for j in range(1, n+1):
            if i == j: fares_dict[i][j] = 0
            else: fares_dict[i][j] = INF

    for start, end, fare in fares:
        fares_dict[start][end] = fare
        fares_dict[end][start] = fare
    

    for k in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if fares_dict[start][end] > fares_dict[start][k] + fares_dict[k][end]:
                    fares_dict[start][end] = fares_dict[start][k] + fares_dict[k][end]
        
    answer = INF
    for k in range(1, n+1):
        answer = min(fares_dict[s][k] + fares_dict[k][a] + fares_dict[k][b], answer)

    return answer  

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))