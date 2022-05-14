def solution(n, lst):
    cache = [-1001 for _ in range(n)]
    cache[0] = lst[0]

    # 연속된 값이므로, 연속을 이어가는게 더 손해라면
    # 누적값을 끊어버릴 수 있다.
    for i in range(1,n):
        cache[i] = max(lst[i], cache[i-1] + lst[i])
    
    print(max(cache))

n = int(input())
lst = list(map(int, input().split()))
solution(n, lst)