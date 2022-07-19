def solution(n, arr1, arr2):
    res = [[' ' for _ in range(n)] for _ in range(n)]
    
    for arr in [arr1, arr2]: 
        for row, num in enumerate(arr):
            col = n-1
            while num > 0:
                num, mod = divmod(num,2)
                if mod == 1:
                    res[row][col] = '#'
                col -= 1
    res = list(map(''.join, res))
    return res

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))