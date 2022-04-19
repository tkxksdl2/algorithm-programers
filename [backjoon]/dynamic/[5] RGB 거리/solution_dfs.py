def solution(cost):    
    min_total = [float('inf')]
    pre = -1
    total = 0
    step(pre, cost, 0, total, min_total)
    
    print(min_total[0])
    return

def step(pre, cost, n, total, min_total):
    if n == len(cost):
        min_total[0] = min(total, min_total[0])
        return

    for v, i in cost[n]:
        if i == pre or total+v >= min_total[0]: 
            continue
        
        step(i, cost, n + 1 , total + v, min_total)

n = int(input())

# [[v, 0], [v, 1], [v, 2]]
cost =  []
for _ in range(n):
    c = list(map(int, input().split()))
    for i, v in enumerate(c):  
        c[i] = [v,i]
    c.sort()    
    cost.append(c)

solution(cost)