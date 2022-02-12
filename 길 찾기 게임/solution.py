from collections import deque
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
        
        tree[node[2]] = {'child':[], 'xy':(node[0],node[1])}
        depth_list[-1].append(node[2])
        
        if len(depth_list) ==1: continue

        min_distance = 100000 * 1000000
        min_node = None
        for parents in depth_list[-2]:
            distance = get_distance((node[0],node[1]), tree[parents]['xy'])
            if distance < min_distance:
                min_node = parents
                min_distance = distance
        tree[min_node]['child'].append(node[2])
    pre_list = []
    post_list = []
    order(tree, depth_list[0][0], pre_list)
    order(tree, depth_list[0][0], post_list, pre=False)
    answer = [pre_list, post_list]
    return answer

def get_distance(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

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