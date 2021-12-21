def solution(n, build_frame):
    structure_base = [[n,0] for n in range(n+1)]
    horizon_base = []
    answer = []

    for frame in build_frame:
        point = frame[:2]
        structure = frame[2]
        task = frame[3]

        if not structure: # 기둥
            if task:      # 건설

                if point in structure_base: #건설가능
                    endpoint = [point[0], point[1] + 1]
                    if endpoint[1] > n:
                        continue
                    answer.append([point[0], point[1], structure])
                    structure_base.append(endpoint)
                    horizon_base.append(endpoint)
                    horizon_base.append([endpoint[0]-1,endpoint[1]])
                else:
                    continue

            else:         # 제거
                pass
        else: # 보
            if task:
                if point in horizon_base: #건설가능
                    endpoint = [point[0]+1, point[1]]
                    if endpoint[1] > n:
                        continue
                    answer.append([point[0], point[1], structure])

                    if endpoint + [1] not in answer:    # 다른 보와 연결되지않는다면 기둥 건설 가능
                        structure_base.append(endpoint) 
                                                        # 다음 위치에 다른보나 기둥이 있다면 보 건설 가능
                    if  [endpoint[0], endpoint[1]-1, 0] in answer or  [endpoint[0]+1, endpoint[1], 1] in answer:
                        horizon_base.append(endpoint)

                else:
                    continue           
    
    print(horizon_base)



    
    return answer



build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

sol = solution(5,build_frame)

print(sol)