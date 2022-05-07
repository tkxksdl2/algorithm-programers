import sys

def solution(n, info):
    wires = [0 for _ in range(501)]
    for i, v in info: wires[i] = v

    last_arr = [501]

    for v in wires:
        if v:
            idx = bisect(last_arr, v, 0 , len(last_arr))
            if idx >= len(last_arr):
                last_arr.append(v)
            else:
                last_arr[idx] = v

    print(n-len(last_arr)) 

def bisect(arr, num, s, e):
    if e-s < 1:
        return s

    m = (s + e) // 2
    if num <= arr[m]:
        return bisect(arr, num, s, m)
    else:
        return bisect(arr, num, m+1 ,e)

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
solution(n, info)