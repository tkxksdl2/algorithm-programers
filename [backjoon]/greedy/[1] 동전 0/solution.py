def solution(n, k, lst):
    cnt = 0
    for coin in lst[::-1]:
        c, k = divmod(k, coin)
        cnt += c
    
    print(cnt)

n, k = map(int, input().split())
lst = [int(input())for _ in range(n)]
solution(n, k, lst)