import sys

def solution(n):
    counter = [0] * 8001
    lst = []
    lst_sum = 0
    
    for _ in range(n):
        num = int(sys.stdin.readline())
        lst_sum += num
        lst.append(num)
        counter[num + 4000] += 1
        
    #최빈값 구하기
    mode_cnt = 0
    mode_lst = []
    for num, cnt in enumerate(counter):
        num = num-4000
        if cnt > mode_cnt:
            mode_cnt = cnt
            mode_lst = []
            mode_lst.append(num)
        elif cnt == mode_cnt:
            mode_lst.append(num)

    lst.sort()
    # 평균
    print(round(lst_sum/n))
    # 중앙값
    if n %2 == 1: print(lst[ n//2 ])
    else:         print((lst[n//2] + lst[n//2-1]) / 2)
    # 최빈값
    if len(mode_lst) == 1:  print(mode_lst[0])
    else:                   print(mode_lst[1])
    # 범위
    print(lst[-1] - lst[0])

n = int(sys.stdin.readline())

solution(n)