def solution(n, lst):
    inc = [1 for _ in range(n)]
    dec = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if lst[i] > lst[j]:
                inc[i] = max(inc[i], inc[j] + 1)
            if lst[n-i-1] > lst[n-j-1]:
                dec[n-i-1] = max(dec[n-i-1], dec[n-j-1] + 1)
    
    ans = 0
    for i in range(n):
        ans = max(ans, inc[i] + dec[i] - 1)

    print(inc)
    print(dec)
    print(ans)


n = int(input())
lst = list(map(int, input().split()))

solution(n, lst)