import sys
def solution(n, lst):
    if n <= 2:
        print(sum(lst))
        return

    arr = [0 for _ in range(n)]
    arr1 = [0 for _ in range(n)]
    arr2 = [0 for _ in range(n)]
    
    arr[0] = arr1[0] = lst[0]
    arr[1] = arr[0] + lst[1]; arr1[1] = lst[1]

    arr2[:3] = lst[:3] 

    for i in range(2, n):
        arr[i] = lst[i] + max(arr[i-2], arr1[i-1], arr2[i-1])
        arr1[i] = lst[i] + arr[i-2]
        
        if i>=3:
            arr2[i] = lst[i] + arr[i-3]

    print(max(arr[-2:]))
 
n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
solution(n, lst)