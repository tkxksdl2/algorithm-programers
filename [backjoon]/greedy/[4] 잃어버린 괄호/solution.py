import re
def solution(s):
    p = re.compile('[+-]*\d+')
    arr = list(map(int,p.findall(s)))
    ans = 0; isminus = False
    for i in arr:
        if isminus and i >= 0:
            ans -= i
        elif i <= 0:
            ans += i
            isminus = True
        else:
            ans += i
    
    print(ans)

s = input()
solution(s)