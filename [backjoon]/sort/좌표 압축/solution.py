import sys
def solution(n, lst):
    lstb = list(set(lst))
    lstb.sort()
    comp_dict = dict()
    for i, v in enumerate(lstb):
        comp_dict[v] = i
    
    for i, v in enumerate(lst):
        lst[i] = comp_dict[v]

    return lst

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst = solution(n, lst)
for v in lst:
    print(v, end=' ')
