def solution(a, b):
    ismatch = [False for _ in range(len(a))]
    idx_lst = [501 for _ in range(len(b))]

    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                if not ismatch[j]:
                    idx_lst[i] = j; ismatch[j] = True
                    break
                else:        
                    idx_lst[i] = j
    print(idx_lst)
    print(ismatch)

    lcs = [1 for _ in range(len(idx_lst))]
    for i in range(len(lcs)):
        for j in range(i):
            if idx_lst[j] < idx_lst[i]:
                lcs[i] = max(lcs[i], lcs[j] + 1)
    
    print(lcs)
    print(lcs[-1])

a = input()
b = input()

solution(a, b)