def solution(n, s, a, b, fares):

    fares_dict = dict()
    for start, end, fare in fares:
        if start not in fares_dict:
            fares_dict[start] = {end:fare}
        else:
            fares_dict[start][end] = fare
        if end not in fares_dict:
            fares_dict[end] = {start:fare}
        else:
            fares_dict[end][start] = fare
    
    print(fares_dict)

    root_a = []
    root_b = []

    node_used=[s]
    fare_res =[]

    dfs(n,s,a,b, fares_dict, node_used, fare_res, root_a, root_b)

    answer = 100000 * (n-1)
    
    for a in root_a:
        for b in root_b:
            temp = 0
            for i in range(len(a)):
                if i <len(b) and a[i] == b[i]:
                    continue
                temp += a[i][2]
            for i in range(len(b)):
                temp += b[i][2]

            if temp < answer:
                answer = temp

    return answer

def dfs(n, s, a, b, fares_dict, node_used, fare_res, root_a, root_b):
    if s == a:
        root_a.append(fare_res.copy())

    if s == b:
        root_b.append(fare_res.copy())

    if len(node_used) == n:
        return

    for end, fare in fares_dict[s].items():
        if end not in node_used:
            node_used.append(end)
            fare_res.append([s, end, fare])
            dfs(n, end, a, b,  fares_dict, node_used, fare_res, root_a, root_b)
            node_used.pop()
            fare_res.pop()       

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))