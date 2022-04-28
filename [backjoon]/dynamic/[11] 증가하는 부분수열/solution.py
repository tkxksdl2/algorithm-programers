def solution(n, lst):
    last_arr = [lst[0]]

    for i in range(1, n):
        idx = bisect(last_arr, lst[i], 0, len(last_arr))
        if idx >= len(last_arr):
            last_arr.append(lst[i])
        else:
            last_arr[idx] = lst[i]

    print(len(last_arr))

def bisect(arr, num, s, e):
    if e-s < 1:
        return s

    m = (s + e) // 2
    if num <= arr[m]:
        return bisect(arr, num, s, m)
    else:
        return bisect(arr, num, m+1 ,e)

n = int(input())
lst = list(map(int, input().split()))
solution(n, lst)

# arr는 길이가 i 인 수열의 마지막값.

# 테스트 코드
# 12
# 1 2 3 4 100 5 6 7 8 9 101 0
# 0 2 3 4 5 6 7 8 9 101     