def solution(n, s, a, b, fares):
    root_a = []
    root_b = []

    node_used=[s]
    fare_res =[]
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

    dfs(n,s,a,b, fares_dict, node_used, fare_res, root_a, root_b)

    print(root_a)
    print(root_b)

    return

def dfs(n, s, a, b, fares_dict, node_used, fare_res, root_a, root_b):
    if s == a:
        print(node_used)
        root_a.append([node_used.copy(),fare_res.copy()])

    if s == b:
        print(node_used)
        root_b.append([node_used.copy(), fare_res.copy()])

    if len(node_used) == n:
        return


    for end, fare in fares_dict[s].items():
        if end not in node_used:
            node_used.append(end)
            fare_res.append(fare)
            dfs(n, end, a, b,  fares_dict, node_used, fare_res, root_a, root_b)
            node_used.pop()
            fare_res.pop()       

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)