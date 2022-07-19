### 동굴 탐험
link : [동굴 탐험 kakao 2020](https://programmers.co.kr/learn/courses/30/lessons/67260/)

-----------------------------------

bfs를 이용한 트리 탐색문제.

일반적인 문제보다 추가된 부분은, 특정 노드끼리에 선행-후행관계가 있다는 점이다.

선행할 노드를 먼저 방문하지 않고는 후행 노드를 방문할 수 없다.

하지만 트리 탐색에 이러한순서를 일일히 적용할 수는 없으므로,

두 가지 경우에 대해 생각해보아야 한다.

1. 선행을 먼저 방문하고 후행을 방문하게 될 경우

    후행 노드를 방문 제약을 제거히여 일반적으로 탐색하도록 한다.

2. 후행을 먼저 방문하게 될 경우

    후행 노드를 일반적으로 진행하도록 두지 않고, wating에 넣어 대기시킨다.

    이후 선행노드를 방문하게 된다면 현재 탐색 상태중에 선행-후행 순서가 가능한 것이므로

    후행 노드를 큐의 다음에 넣어 탐색시킨다.

    끝까지 선행노드를 방문하지 않는다면 이 후행노드는 방문할 수가 없는 것이므로 전체 순회도

    불가능해진다.


이를 위해 선행 노드정보 pre, 후행 노드정보, 선행-후행 관계 order, 

trail_block, 방문 여부 visited, 대기노드 wating이 필요하다.


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

다음 노드가 이미 방문한 노드라면 넘어간다.

막혀있는 후행노드라면 대기시킨다.

선행노드라면 후행노드의 제약을 풀고, 후행노드가 대기중이라면 출발시킨다.

일반 노드라면 일반적인 탐색을 돈다.

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


모든 탐색을 끝마친 후, 탐색한 노드의 개수가

전체 노드 개수와 같다면 전체를 탐색한 것이므로 True, 아니면 False를 반환한다.


        if len(visited) == n:
        return True

    return False