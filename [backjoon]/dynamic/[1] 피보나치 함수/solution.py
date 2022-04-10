lst = [0, 1]
def solution(n):
    if n == 0:
        return (1, 0)
    return (fibonacci(n-1), fibonacci(n))

def fibonacci(n):
    if n == 0 : 
            return 0
    elif n == 1 : 
            return  1
    elif n >= len(lst):
        f = fibonacci(n-1) + fibonacci(n-2)
        lst.append(f)
        return f
    else:
        return lst[n]

n = int(input())
ans = []
for _ in range(n):
    ans.append(solution(int(input())))
for z, o in ans:
    print(z, o)