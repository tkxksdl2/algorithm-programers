def solution(n):
    global n_lst
    n_lst = [0, 0, 1, 1] + [-1] * 10**6

    for num in range(n+1):
        if num <= 3: continue

        if not num % 3 and not num % 2:
            n_lst[num] = min(n_lst[num//3], n_lst[num//2], n_lst[num-1]) + 1
        elif not num % 3:
            n_lst[num] = min(n_lst[num//3], n_lst[num-1]) + 1
        elif not num % 2:
            n_lst[num] = min(n_lst[num//2], n_lst[num-1]) + 1
        else:
            n_lst[num] = n_lst[num-1] + 1
    
    print(n_lst[n])


solution(int(input()))  