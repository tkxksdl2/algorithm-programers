def solution(n):
    num, cnt = 666, 1

    while cnt < n:
        num +=1
        if '666' in str(num):
            cnt += 1
    return num
print(solution(int(input())))