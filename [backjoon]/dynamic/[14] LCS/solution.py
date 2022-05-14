def solution(a, b):
    acc_lst = [0 for _ in range(len(a))]

    for word in b:
        cnt = 0
        for i in range(len(acc_lst)):
            if cnt < acc_lst[i]:
                cnt = acc_lst[i] #이전 최대 누적값을 가져감
            elif word == a[i]:  #이전 최대 누적값에 +1 해서 저장
                acc_lst[i] = cnt + 1
        
    print(max(acc_lst))

a = input()
b = input()

solution(a, b)