def solution(n):
    lst = [[0 for _ in range(10)] for _ in range(n+1)]

    lst[1] = [1 for _ in range(10)]

    for i in range(2, n+1):
        for j in range(1, 9):
            lst[i][j] = (lst[i-1][j-1] + lst[i-1][j+1]) % 10**9
        
        lst[i][0] = lst[i-1][1] 
        lst[i][9] = lst[i-1][8]
    
    print(sum(lst[n][1:]) % 10**9 )


solution(int(input()))

    # 앞자리가 0인경우 = 직전 앞자리 1인경우
    # 앞자리가 i(1<i<9) = 직전 앞자리 i-1인경우 + i+1인경우
    # 앞자리가 9인경우 = 직전 앞자리 8인경우