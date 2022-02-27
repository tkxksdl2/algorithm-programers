from collections import deque

def solution(n, path, order):
    cave = dict()
    for i in range(n):
        cave[i] = {'sibling':[]}
    
    for p in path:
        s,e = p
        cave[s]['sibling'].append(e)
        cave[e]['sibling'].append(s)

    pre = set([x[0] for x in order])
    trail_block = set(x[1] for x in order)
    order = {x[0]:x[1] for x in order}

    q = deque([0])
    visited = set()
    wating = set()

    while q:
        next = q.popleft()

        # 중복이나 조건 위반
        if next in visited:
            continue
        if next in trail_block:
            wating.add(next) 
            continue

        # 도착한 경우
        if next in pre:
            # 선행을 밟았을 때 후행을 이미 방문했다면, 후행에서부터 출발.
            if order[next] in wating:
                q.append(order[next])
            trail_block.remove(order[next])
        
        q += cave[next]['sibling']
        visited.add(next)

    if len(visited) == n:
        return True

    return False


n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order =	[[8,5],[6,7],[4,1]]

print(solution(n,path,order))