from collections import deque

def solution(board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    n = len(board)
    checked = set([(0,0)])
    cost_dict = {(0,0):0}
    res = deque([(0,0,-1,0)])
    max_corner = 0
    checking_temp = set()
    answer = []

    while res:
        y, x, corner, cost = res.popleft()

        if corner+1 >max_corner:
            max_corner += 1
            checked = checked.union(checking_temp)
            checking_temp = set()

        if y == n-1 == x:
            answer.append(cost + 500 * corner)

        for i in range(4):
            next = (y+dy[i], x+dx[i], corner+1, cost+100)

            while 0<= next[0] < n and 0 <= next[1] < n and \
                ((next[0], next[1]) not in checked or cost < cost_dict[(next[0],next[1])])\
                and board[next[0]][next[1]] == 0:

                res.append(next)
                cost_dict[(next[0],next[1])] = cost
                checking_temp.add((next[0], next[1]))
                next = (next[0]+dy[i], next[1]+dx[i], corner +1 ,next[3]+100)

    return min(answer)

board = [[0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,1,0,0,0,1],
         [0,0,1,0,0,0,1,0],
         [0,1,0,0,0,1,0,0],
         [1,0,0,0,0,0,0,0]]
         
print(solution(board))
