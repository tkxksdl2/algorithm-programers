import sys
sys.setrecursionlimit(10005)

def solution(k, num, links):
    tree = dict()
    start = int()

    for i, v  in enumerate(num):
        tree[i] = {'root':-1, 'next' : [], 'value': v}

    for i in tree: 
        for dir in links[i]:
            tree[i]['next'].append(dir)
            if dir != -1:
                tree[dir]['root'] = i

    for i in range(len(num)):
        if tree[i]['root'] == -1:
            start = i
            break

    max_scale = sum(num)
    min_scale = (max_scale//k) +1 if (max_scale % k) > 0 else  max_scale//k 
    min_scale = max(max(num), min_scale)

    while min_scale < max_scale:
        global subcnt
        subcnt = 1
        
        limit_scale = (min_scale + max_scale) //2
        post_sub(tree, start, limit_scale , k)
        
        if subcnt > k:
            min_scale = limit_scale + 1
        elif subcnt <= k:
            max_scale = limit_scale

    return min_scale
        

def post_sub(tree, start, limit_scale, k):
    global subcnt
    # 루트노드일 경우 값을 반환하고 탈출.
    if tree[start]['next'][0] == tree[start]['next'][1] == -1:
        return tree[start]['value']

    # 왼쪽 자식 노드값
    left = 0
    if tree[start]['next'][0] != -1:
        left = post_sub(tree, tree[start]['next'][0], limit_scale, k)
    # 오른 쪽 자식 노드값
    right = 0
    if tree[start]['next'][1] != -1:
        right = post_sub(tree, tree[start]['next'][1], limit_scale, k)

    # 조건문 전개
    root_val = tree[start]['value']
    # 양쪽을 다 더해도 작을 경우
    if root_val + left + right <= limit_scale:
        return root_val + left + right
    # 다 더하면 크지만 둘 중 작은 값을 더해도 작을 경우
    min_leaf = min(left, right)
    if root_val + min_leaf <= limit_scale:
        subcnt += 1
        return root_val + min_leaf 
    # 두 자식 모두 더할 수 없는경우
    subcnt +=2
    return root_val


k = 3
num =	[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links =[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

print(solution(k, num, links))