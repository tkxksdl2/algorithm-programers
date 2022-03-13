n, m = map(int, input().split())
board = [input() for _ in range(n)]

def solution(n, m, board):
    answer = float('inf')
    for y in range(n-7):
        for x in range(m-7):

            ws_cnt, bs_cnt = 0, 0
            for i in range(8):
                for j in range(8):
                    if (i+j) %2 == 0: #짝수자리일 경우
                        if board[y+i][x+j] != 'W':
                            ws_cnt +=1
                        if board[y+i][x+j] != 'B':
                            bs_cnt +=1
                    else:
                        if board[y+i][x+j] != 'B':
                            ws_cnt +=1
                        if board[y+i][x+j] != 'W':
                            bs_cnt +=1

                   
            print(answer, bs_cnt, ws_cnt)
            answer = min([answer, bs_cnt, ws_cnt])
    return answer

print(solution(n,m, board))