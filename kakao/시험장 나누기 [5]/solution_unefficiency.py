from itertools import combinations
from collections import deque
def solution(k, num, links):
    if k == 1: return sum(num)

    tree = dict()
    leafs = set()
    for i, v  in enumerate(num):
        tree[i] = {'next' : [], 'value': v}
        for dir in links[i]:
            leafs.add(dir)
            tree[i]['next'].append(dir)

    for i in range(len(num)):
        if i not in leafs:
            start = i
    
    check_link = list(combinations(range(len(num)-1), k-1))
    answer = float('inf')

    for comb in check_link:
    
        sum_lst = [0]
        comb = list(comb)
        info = {'next_cut': comb.pop(0), 'link_count':-1, 'nxt_idx':0}
        preorder(tree, start, comb, sum_lst, info,0)
        answer = min(answer, max(sum_lst))

    return answer

def preorder(tree, s, comb, sum_lst, info, add_idx):
    sum_lst[add_idx] += tree[s]['value']
    q = deque(tree[s]['next'])
    while q:
        next_s = q.popleft()
        if next_s == -1: continue

        info['link_count'] += 1
        if info['link_count'] == info['next_cut']:
            sum_lst.append(0)
            if comb: info['next_cut'] = comb.pop(0)
            info['nxt_idx'] += 1
            preorder(tree, next_s, comb, sum_lst, info, info['nxt_idx'])
        else:
            preorder(tree, next_s, comb, sum_lst, info, add_idx)

k = 2
num = [6,9,7,5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]

print(solution(k, num, links))