def solution(n, lst):
    lst.sort()

    for i in range(1, n):
        lst[i] += lst[i-1]
    
    print(sum(lst))


n = int(input())
lst = list(map(int, input().split()))
solution(n, lst)