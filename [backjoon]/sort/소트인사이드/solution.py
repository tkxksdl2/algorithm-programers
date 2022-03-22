def solution(n):
    counter = [0 for _ in range(10)]
    for num in n:
        counter[9-int(num)] += 1
    
    for num, cnt in enumerate(counter):
        for _ in range(cnt):
            print(9-num, end='')

n = input()
solution(n)
