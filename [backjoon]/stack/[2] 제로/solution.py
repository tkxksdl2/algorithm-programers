import sys
n = int(input())
arr = list()
ans = 0
while n > 0:
    k = int(sys.stdin.readline())
    if not k:
        ans -= arr.pop()
    else:
        ans += k; arr.append(k)
    n -= 1
    
print(ans)