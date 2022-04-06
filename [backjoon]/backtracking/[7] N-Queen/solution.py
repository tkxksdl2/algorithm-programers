def solution(n):
    force = []
    global cnt
    cnt = 0
    
    def dfs(n, py):
        global cnt

        if py == n:
            cnt += 1
            return

        for px in range(n):
            # 이전 퀸들의 값 y, x
            if force:
                isvalid = True
                for y, x in force:
                    if  px == x or abs(y-py) == abs(x-px):
                        isvalid = False
                        break
                if isvalid:
                    force.append([py,px])
                    dfs(n, py+1)

                    force.pop()
            else:
                force.append([py,px])
                dfs(n, py+1)

                force.pop()

        return
       

    dfs(n, 0) 
    
    print('cnt:', cnt)
    return


n = int(input())

solution(n)