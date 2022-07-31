def solution(grid):
    # 상 우 하 좌
    my = [-1, 0, 1, 0]
    mx = [0, 1, 0, -1]
    
    check_dup = set()
    start_points = []
    answer = []
    
    for i in range(len(grid)):
        j = len(grid[0])-1
        start_points.append([i, 0, 1]) # 우
        start_points.append([i, j, 3]) # 좌
    for i in range(len(grid[0])):
        j = len(grid) - 1
        start_points.append([j, i, 0]) # 상
        start_points.append([0, i, 2]) # 하
    
    nexts = []
    end_point = []
    for s in start_points:
        end_point.append(s)
        nexts.append(s)
        cnt = 0
        while nexts:
            cur = nexts.pop(0)
            checking_token = str(cur[0]) + str(cur[1]) + str(cur[2])
            if checking_token in check_dup:
                break
            check_dup.add(checking_token)
            
            next_y = (cur[0] + my[cur[2]]) % len(grid)
            next_x = (cur[1] + mx[cur[2]]) % len(grid[0])
            
            if grid[next_y][next_x] == 'L':
                next_m = (cur[2] + 3) % 4
            elif grid[next_y][next_x] == 'R':
                next_m = (cur[2] + 1) % 4
            else:
                next_m = cur[2]
            cnt += 1

            next_point = [next_y, next_x, next_m]
            if next_point in end_point:
                answer.append(cnt)
                break

            nexts.append(next_point)
    
    return answer

grid = ["SL","LR"]
print(solution(grid))