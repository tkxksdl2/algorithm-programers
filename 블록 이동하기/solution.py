from collections import deque

def solution(board):
    res = deque([Robot(0,0,0,1)])
    checked = set()
    checked.add(((0,0),(0,1)))
    n = len(board)

    while res:
        R = res.popleft()
        
        if R.isfinished(n):
            return R.count
        
        # 평행이동
        for i in range(4):
            NextR = R.move(i)
            NextR.count = R.count+1

            if NextR.isvalid(n,board) and (NextR.getxy() not in checked and NextR.getxy2() not in checked):
                res.append(NextR)
                checked.add(NextR.getxy())

        # 회전
        for i in range(4):
            if R.move(i).isvalid(n, board):
                Nexts = R.turn(i)
                for NextR in Nexts:
                    NextR.count = R.count+1
                    
                    if NextR.isvalid(n, board) and (NextR.getxy() not in checked and NextR.getxy2() not in checked):
                        res.append(NextR)
                        checked.add(NextR.getxy())

    return -1


class Robot():

    def __init__(self, y1, x1, y2, x2):
        self.y1, self.x1, self.y2, self.x2 = y1, x1, y2, x2
        ########## 상, 하, 좌, 우
        self.my = [-1, 1, 0, 0]
        self.mx = [ 0, 0,-1, 1]
        self.count = 0

    def move(self, direction : int):
        return Robot(self.y1 + self.my[direction], self.x1 + self.mx[direction], self.y2 + self.my[direction], self.x2 + self.mx[direction])
        
    
    def turn(self, direction : int):
        return (Robot(self.y1, self.x1, self.y1 + self.my[direction], self.x1 + self.mx[direction]) ,        # y1,x1이 중심
                Robot(self.y2 + self.my[direction], self.x2 + self.mx[direction], self.y2, self.x2))    # y2, x2가 중심

    def isvalid(self, n, board):
        return self.y1 >= 0 and self.x1 >=0 and self.y2 >= 0 and self.x2 >=0 and \
                self.y1 < n and self.x1 < n and self.y2 < n and self.x2 < n and \
                not board[self.y1][self.x1] and not board[self.y2][self.x2]

    def isfinished(self, n):
        return (self.y1 == n-1 and self.x1 == n-1) or (self.y2 == n-1 and self.x2 == n-1)

    def getxy(self):
        return ((self.y1, self.x1), (self.y2 ,self.x2))
    def getxy2(self):
        return ((self.y2 ,self.x2), (self.y1, self.x1))



s = solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
print(s)
