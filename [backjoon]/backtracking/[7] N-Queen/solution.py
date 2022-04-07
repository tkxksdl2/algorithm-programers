def solution(n):
    global cnt
    cnt = 0

    checkcol = [True for _ in range(n)]
    check_rs = [True for _ in range(2*n)] # 우상향 대각선
    check_ls = [True for _ in range(2*n)] # 좌상향 대각선

    def dfs(n, py):
        global cnt

        if py == n:
            cnt += 1
            return

        for px in range(n):
            if checkcol[px] and check_rs[py+px] and check_ls[py-px+n-1]:
                checkcol[px] = check_rs[py+px] = check_ls[py-px+n-1] = False
                dfs(n, py+1)
                checkcol[px] = check_rs[py+px] = check_ls[py-px+n-1] = True

            # for y, x in force:
            #     if  px == x or abs(y-py) == abs(x-px):
            #         isvalid = False
            #         break
            
        return

    dfs(n, 0)
    print( cnt)
    return


n = int(input())

solution(n)