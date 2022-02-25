def solution(n, path, order):
    cave = dict()
    for i in range(n):
        cave[i] = {'sibling':[]}
    
    for p in path:
        s,e = p
        cave[s]['sibling'].append(e)
        cave[e]['sibling'].append(s)

    blocked = set(x[1] for x in order)
    dest = set([x[0] for x in order])
    order = {x[0]:x[1] for x in order}
    start = 0

    while dest:
        q = cave[start]['sibling'].copy()
        visited = set([start])
        next_d = bfs(q, cave, dest, blocked, visited, order)
        if next_d:
            start = next_d
        else:
            return False

    return True

def bfs(q, cave, dest, blocked, visited, order):
    while q:
        print(q)
        next = q.pop(0)
        
        print(next)
        # 중복이나 조건 위반
        if next in blocked or next in visited: 
            continue

        # 도착한 경우
        if next in dest:
            blocked.remove(order[next])
            dest.remove(next)
            return next
        
        q += cave[next]['sibling']
        visited.add(next)
    
    return False
    



n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order =	[[8,5],[6,7],[4,1]]

print(solution(n,path,order))