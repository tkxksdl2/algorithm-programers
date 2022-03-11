n = input()
def solution(n):
    n_len = len(n)
    n = int(n)
    for i in range(max(0, n-9*n_len), n):
        decompose = i
        for digit in str(i):
            decompose += int(digit)
        if decompose == n:
            return i
    return 0

print(solution(n))