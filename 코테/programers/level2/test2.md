## 빛의 경로 사이클

Link : [빛의 경로 사이클 skill check level2](hhttps://school.programmers.co.kr/learn/courses/30/lessons/86052)

---

dfs를 이용해 이차원 배열을 순회하는 문제

배열 밖으로 진행 방향이 나가면 다시 반대쪽에서 돌아오기 때문에 어떤 경로든 무조건 배열 내부에서 순환하게 된다.

하나의 경로는 하나의 순환에서만 존재하므로, 경로를 따라 진행하다 시작 위치로 돌아오면, 그경로들은 그 순환에만 배정된다.

따라서 하나의 경로를 방문했다면 그 경로는 다시 방문할 필요가 없으므로 중복검사를 통해 걸러주면 된다.

다만 한 위치를 방문하더라도 어느 방향으로 진행하느냐도 중요하다. 따라서 중복검사를 할 경로의 개수는 y _ x _ 4(=진행방향) 이다.

```python
    check_visit = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
```

다만 시작지점을 잡을 때 오류가 있었다. 처음 나는 시작 지점이 가장자리에서 안쪽으로 들어온다는 것만 생각하고 시작지점을 설정했다.

그러나 배열이 커졌을 때, 내부에서만 순환하는 경로가 있을 수 있다. 이 경우 가장자리와의 접점이 전혀 없으므로 올바른 답을 포함할 수 없다.

이 외에도 생각하지 못한 다른 많은 경우를 포함할 수 없다. 따라서 올바른 시작지점은 모든 위치에서 모든 방향으로 시작하도록 하는 것이다.

```python
    start_points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for m in range(4):
                start_points.append([i, j, m])
```

다음은 각 시작 위치에서 올바른 방향으로 경로를 탐색해준다. 미리 지정한 my,mx 방향에 따라 경로를 꺾어주기만 하면 된다. 다만 여기서 my, mx의 방향은 상, 하, 좌, 우 가 아니라 상, 우 ,하, 좌 이다. 진행방향을 좌, 우로 회전해야 하기 때문에 이 방향 배열도 회전하는 순서대로 배치해줘야 my, mx의 인덱스를 바꿀 때 일관적이다.

```python
    #      상 우 하 좌
    my = [-1, 0, 1, 0]
    mx = [0, 1, 0, -1]
    ##~~~~~~~~~~~~~~~~~~##

    while nexts:
            cur = nexts.pop()

            next_y = (cur[0] + my[cur[2]]) % len(grid)
            next_x = (cur[1] + mx[cur[2]]) % len(grid[0])

            if grid[next_y][next_x] == 'L':
                next_m = (cur[2] - 1) % 4
            elif grid[next_y][next_x] == 'R':
                next_m = (cur[2] + 1) % 4
            else:
                next_m = cur[2]
```

나머지는 미리 설정한 중복 검사 배열 `check_vist`에 따라 중복을 거르고, 시작지점으로 돌아오면 개수를 넣어주면 된다.

```python
            cnt += 1
            next_point = [next_y, next_x, next_m]

            if next_point == end_point:
                answer.append(cnt)
            elif not check_visit[next_y][next_x][next_m]:
                nexts.append(next_point)
            check_visit[next_y][next_x][next_m] = True
```
