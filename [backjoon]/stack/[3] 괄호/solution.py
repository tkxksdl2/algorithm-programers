import sys
n = int(input())

for _ in range(n):
    s = sys.stdin.readline().strip()
    point = 0
    for w in s:
        if w == '(': point += 1
        else:        
            point -= 1
            if point < 0: break
        
    if point == 0: print('YES')
    else:          print('NO')