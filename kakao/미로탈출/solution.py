import heapq

def bit_mask(state, trap_idx, destination, flag):
    if flag == 1: # 특정위치 함정의 토글상태를 반환.
        return (1 & (state >> trap_idx[destination])) 
    else: # 특정위치 함정을 토글. 즉 state를 return
        return state ^ (1 << trap_idx[destination]) 

def solution(n, start, end, roads, traps):
    answer = 0
    INF = float('inf')
    
    graph = {i:[] for i in range(1,n+1)}
    for road in roads:
        x, y, cost = road
        graph[x].append([y,cost,0])
        graph[y].append([x,cost,1])


    # 함정들의 토글상태를 나타내기위한 비트 인덱스
    trap_idx ={v:i for i,v in enumerate(traps)}
    # 함정들의 토글상태 조합마다 다른 최소거리를 저장한다.
    dp = [[INF for _ in range(n+1)] for _ in range(2**len(traps))]

    

    
    node_list = []
    heapq.heappush(node_list, (0,start,0)) #누적거리, 목적지, 상태
    dp[0][start] = 0

    while node_list:
        current_distance, current_destination, state = heapq.heappop(node_list)

        if end == current_destination:
            answer = current_distance
            break
        
        if dp[state][current_destination] < current_distance:
            continue 
        
        for next_destination, distance, flag in graph[current_destination]:
            next_state = state
            if current_destination in traps:
                # 다음 목적지도 트랩
                if next_destination in traps:
                    pre = bit_mask(state, trap_idx, current_destination, 1)
                    nxt = bit_mask(state, trap_idx, next_destination, 1)
                    
                    # 이번 간선의 상태는 양쪽 노드의 토글상태에 따라 달라진다.
                    # 합계가 짝수면 0, 홀수면 1이므로 논리적으로 xor연산과 같다.
                    cur_flag = pre ^ nxt
                    next_state = bit_mask(state, trap_idx, next_destination, 2)
                else:
                    cur_flag = bit_mask(state, trap_idx, current_destination, 1)
            
            else:
                if next_destination in traps:
                    cur_flag = bit_mask(state, trap_idx, next_destination, 1)
                    next_state = bit_mask(state, trap_idx, next_destination, 2)
                else:
                    cur_flag = 0
            
            if cur_flag == flag: #저장된 노드의 방향이 현재 state 상태에 따른 방향과 같은지 검증
                if dp[next_state][next_destination] > current_distance + distance:
                    dp[next_state][next_destination] = current_distance + distance
                    heapq.heappush(node_list, (dp[next_state][next_destination], next_destination, next_state))

    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2,3]

print(solution(n, start, end, roads, traps))