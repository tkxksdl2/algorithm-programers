def solution(n, m, lst):
    remain = [0 for _ in range(m)]
    res = 0

    for i in range(0, n):
        res = (res + lst[i]) % m
        remain[res] += 1

    cnt = remain[0] # 기본 자리수 자체가 0인 경우
    for num in remain:
        cnt += comb(num)

    print(cnt)

def comb(num):
    if num < 2: return 0

    return num * (num-1) // 2


n, m = map(int, input().split())
lst = list(map(int, input().split()))
solution(n, m, lst)