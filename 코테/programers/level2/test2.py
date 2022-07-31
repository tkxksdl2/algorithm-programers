def solution(grid):
    # 상 우 하 좌
    my = [-1, 0, 1, 0]
    mx = [0, 1, 0, -1]

    check_visit = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    start_points = []
    answer = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for m in range(4):
                start_points.append([i, j, m])

    nexts = []
    for s in start_points:
        y, x, m = s
        if check_visit[y][x][m]:
            continue

        end_point = [y, x, m]
        nexts.append(s)
        cnt = 0
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
            
            cnt += 1
            next_point = [next_y, next_x, next_m]
            
            if next_point == end_point:
                answer.append(cnt)
            elif not check_visit[next_y][next_x][next_m]:
                nexts.append(next_point)
            check_visit[next_y][next_x][next_m] = True

    answer.sort()
    return answer

grid = ["SL", "LS","SL"]
print(solution(grid))