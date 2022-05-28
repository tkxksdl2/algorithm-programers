def solution(n, k, arr):
    ans = acc = 0
    for i in range(k):  acc += arr[i]; ans = acc

    for i in range(k, n):
        acc += arr[i]; acc -= arr[i-k] 
        if acc > ans:
            ans = acc

    print(ans)

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
solution(n, k, arr)