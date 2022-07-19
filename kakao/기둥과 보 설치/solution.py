def solution(n, build_frame):
    answer = set()

    for frame in build_frame:
        x, y, structure, task = frame

        if structure: # 보
            if task:
                if check_floor_build(x, y, answer):
                    answer.add((x, y, 1))
            else:
                answer.remove((x,y,1))
                for a_x, a_y, a_s in answer:
                    if a_s == 1:
                        check = check_floor_build(a_x, a_y, answer)
                    else:
                        check = check_pillar_build(a_x, a_y, answer)

                    if not check:
                        answer.add((x,y,1))
                        break 

        else:       # 기둥
            if task:
                if check_pillar_build(x, y, answer):
                    answer.add((x, y, 0))
            else:
                answer.remove((x,y,0))
                for a_x, a_y, a_s in answer:
                    if a_s == 1:
                        check = check_floor_build(a_x, a_y, answer)
                    else:
                        check = check_pillar_build(a_x, a_y, answer)

                    if not check:
                        answer.add((x,y,0))
                        break 
    
    answer = [list(i) for i in answer]
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    
    return answer

def check_pillar_build(x, y, answer):
    if y == 0 or (x,y-1,0) in answer or (x-1,y, 1) in answer or (x,y, 1) in answer:
        return True

    return False

def check_floor_build(x, y, answer):
    if ((x-1, y, 1) in answer and (x+1, y, 1) in answer) or (x, y-1, 0) in answer or (x+1, y-1, 0) in answer:
        return True

    return False

    

#build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5
sol = solution(n,build_frame)

print(sol)