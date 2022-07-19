import heapq

def solution(n, s, a, b, fares):
    global INF
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
    
    answer = INF

    for k in range(1, n+1):
        answer = min(dijkstra(fares_dict,s)[k] + dijkstra(fares_dict,k)[a] + dijkstra(fares_dict,k)[b], answer)

    return answer  

def dijkstra(graph, start):
    # 시작지점에서 각 노드까지의 거리
    distances = {node: INF if node != start else 0 for node in graph}
    queue = []
    heapq.heappush(queue, [distances[start], start]) 

    while queue:
        # 거리, 행선지 가장 거리가 짧은 것 부터 호출함
        current_distance, current_destination = heapq.heappop(queue)

        # 만약 누적된 거리가 이미 현 최소거리보다 길어지면 넘어감
        if current_distance > distances[current_destination]:
            continue

        # 현재 도착한 지점에서 각 노드까지의 거리를 꺼냄
        for new_destination, new_distance in graph[current_destination].items():
            # 거리 = 현재 누적 거리 + 도착지점에서 노드까지의 거리
            distance = current_distance + new_distance
            #현재 저장된 최소거리보다 계산된 거리가  더 짧다면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                #누적 거리와 도착한 지점을 다시 전달
                heapq.heappush(queue, [distance, new_destination])

    return distances
    

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n,s,a,b,fares))