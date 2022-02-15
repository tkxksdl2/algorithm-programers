def solution(k, num, links):
    answer = 0
    tree = dict()

    for i, v  in enumerate(num):
        tree[i] = {'next' : [], 'value': v}
        for dir in links[i]:
            if dir == -1:
                tree[i]['next'].append(None)
            else:
                tree[i]['next'].append(dir)
    
    print(tree)

    return answer

k = 3
num =[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

print(solution(k, num, links))