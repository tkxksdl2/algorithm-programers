import sys
n = int(sys.stdin.readline())
stack = []; ans = []
push_cnt = 1

for _ in range(n):
    s = int(sys.stdin.readline())
     # 이번에 넣을 숫자가 있는 부분까지 계속 push
    while push_cnt <= s:
        stack.append(push_cnt)
        ans.append('+'); push_cnt += 1
    last_push = stack.pop()

    if last_push == s:
        ans.append('-')
    else:
        ans = ['NO']
        break

for a in ans: print(a)
