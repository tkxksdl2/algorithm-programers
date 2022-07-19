from collections import deque
import sys
sys.setrecursionlimit(20000)

def solution(nodeinfo):
    nodeinfo = [value +[i+1] for i, value in enumerate(nodeinfo)]
    nodeinfo.sort(key= lambda x: (-x[1], x[0]))

    depth_list = []
    y_min = 100001
    tree = dict()

    for node in nodeinfo:
        if node[1] < y_min:
            depth_list.append([])
            y_min = node[1]

        tree[node[2]] = {'child':[], 'xy':[node[0],node[1]]}
        depth_list[-1].append(node[2])

        if len(depth_list) ==1:
            tree[node[2]]['bound'] = [-1, 100001]
            continue

        for parents in depth_list[-2]:
            if  tree[parents]['bound'][0] < node[0] < tree[parents]['xy'][0]:
                tree[node[2]]['bound'] = [tree[parents]['bound'][0], tree[parents]['xy'][0]]
                tree[parents]['child'].append(node[2])
                break
            elif tree[parents]['xy'][0] < node[0] < tree[parents]['bound'][1]:
                tree[node[2]]['bound'] = [tree[parents]['xy'][0], tree[parents]['bound'][1]]
                tree[parents]['child'].append(node[2])
                break

    pre_list = []
    post_list = []
    order(tree, depth_list[0][0], pre_list)
    order(tree, depth_list[0][0], post_list, pre=False)
     
    return [pre_list, post_list]

def order(tree, start, res, pre=True):
    if pre: res.append(start)
    q = deque(tree[start]['child'])
    while q:
        if pre: order(tree, q.popleft(), res)
        else:   order(tree, q.popleft(), res, pre=False)
    if not pre: res.append(start)
    return


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))