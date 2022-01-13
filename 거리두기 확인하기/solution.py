def solution(places):
    answer = []

    for room in places:
        answer.append(check(room))
    return answer

def check(room):
    dy = [-1,1,0,0] #상 하 좌 우
    dx = [0,0,-1,1]
    for y in range(len(room)):
        for x in range(len(room[0])):

            if room[y][x] == 'P':
                for i in range(4):
                    nxt_y = y+dy[i]
                    nxt_x = x+dx[i]
                    if  0<= nxt_y < 5 and 0 <= nxt_x < 5:
                        if room[nxt_y][nxt_x]=='P':
                            return 0
                        elif room[nxt_y][nxt_x]=='O':
                            if 0 <= nxt_y+dy[i] < 5 and  0 <= nxt_x+dx[i] < 5:   
                                if room[nxt_y+dy[i]][nxt_x+dx[i]]=='P':
                                    return 0
                            
                            if i <=1: # 일전에 상하좌우 중 어느방향을 보았는가에 따라 대각선검색
                                checktype = [2,3]
                            else:
                                checktype = [0,1]
                            
                            for i in checktype:
                                if 0 <= nxt_y+dy[i] <5 and 0 <= nxt_x+dx[i] < 5:
                                    if room[nxt_y+dy[i]][nxt_x+dx[i]]=='P':
                                        return 0


    return 1


places = [["POOOP", 
           "OXXOX", 
           "OPXPX", 
           "OOXOX", 
           "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))