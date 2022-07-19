### 합승 택시 요금
link : [합승 택시 요금 카카오 2021 ](https://programmers.co.kr/learn/courses/30/lessons/72413)

-----------------------------------

노드를 탐색하는 경로 문제. 목적지는 두 종류가 있고,

이 두 목적지까지 가는 경로 두 개가 얼마나 겹치는가에 따라 비용이 낮아지고,

이 중 가장 비용이 낮은 경우의 수의 비용을 찾는 문제.

일단 경로를 탐색한다는 것 부터 dfs를 사용해야 한다고 생각했다.

그래서 처음에 dfs를 이용해 각 목적지까지 가는 모든경우의 수를 찾아내는 것에 성공했다.

그러나 이 방법으로는 그 이후 각 경로가 겹치는 부분을 검사할 때

모든 a루트 경로 * 모든 b 루트 경로 의 복잡도를 가지게 되기 때문에

너무 많은 시간이 걸렸다.

새로운 방법을 찾아내야 할 필요가 있다.

------------------------------------

새로운 방법으로 최소경로를 구하는 두 가지 알고리즘을 찾아보았다.

최소경로 문제에는 플로이드 와샬 알고리즘과 다익스트라 알고리즘을 사용하는데,

먼저 플로이드 와샬 알고리즘을 사용해서 문제를 풀었다.

이는 출발지와 목적지 사이에 중간지점을 둠으로써 중간지점을 거치는 거리가 더 짧다면

최소거리를 갱신하는 알고리즘이다

시작지, 목적지, 중간지점까지 세번의 n루프를 돌아야 하기 때문에

O(N^3)의 복잡도를 가지지만, 노드개수인 N은 최대가 200 뿐이므로 문제풀이가 가능했다.

    for k in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if fares_dict[start][end] > fares_dict[start][k] + fares_dict[k][end]:
                    fares_dict[start][end] = fares_dict[start][k] + fares_dict[k][end]
        
    answer = INF
    for k in range(1, n+1):
        answer = min(fares_dict[s][k] + fares_dict[k][a] + fares_dict[k][b], answer)

노드 비용 그래프를 잘 초기화 해놓는다면 이렇게 알고리즘 부분 코드가 간단해진다.

이 방법은 모든 노드에서 노드까지의 최소거리를 구하는것이 가능하다.

---------------------------------------

다음으로는 다익스트라를 사용해 구현해 보았다.

다익스트라 자체가 코드 구현이 더 복잡해 이해하는데 약간 애를 먹었다.

다익스트라 알고리즘은 시작지점하나에서 다른 지점까지의 최소거리를 구할 수 있다.

그래서 이 문제의 경우 (시작지점 s 부터 합승하는 지점 k까지의 거리) + (k부터 a까지) + (k부터 b까지) 

총 세번의 다익스트라 호출이 필요하다.

거리를 기반으로 다음 노드를 찾기 때문에, 이전엔 dfs를 했던것과 달리

방문했던 노드를 거를 필요가 없다는 사실이 흥미롭다.

방문했던 노드를 다시 방문하는 경우는 이미 그 경로에서의 누적거리보다 많아지기 때문에

조건문제서 걸러지게 된다.

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

다만 코드가 복잡하고, 어차피 합승지점에 따라 여러 번 반복호출해야 하기 때문에

이 문제의 경우 플로이드 와샬보다 성능이 좋지 않았다.

플로이드 와샬은 처음부터 모든 노드에서 노드 간 최소 거리를 구하기 때문에

분기를 나누거나 알고리즘을 반복호출할 필요가 없다.

고로 출제의도는 플로이드 와샬을 쓰는 것이 맞았던 것 같다.

