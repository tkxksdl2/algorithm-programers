n = int(input())
def solution(n):
    num = 666
    cnt = 1
    while cnt < n:
        num +=1
        if '666' in str(num):
            cnt += 1
    return num
print(solution(n))