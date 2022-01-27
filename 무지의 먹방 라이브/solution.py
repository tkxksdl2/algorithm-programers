
def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    
    food_times = [[t,i] for i,t in enumerate(food_times)]
    food_times.sort()

    n_remain = len(food_times)
    min = 0

    for idx, v in enumerate(food_times):
        t = v[0]
        
        if t == min : 
            n_remain -= 1
            continue
        elif t > min and (t-min) * n_remain <= k:
            k -= (t-min) * n_remain
            min = t
            n_remain -= 1
        
        elif k < (t-min) * n_remain:
            k %= n_remain
            res = food_times[idx:]
            res.sort(key= lambda x: x[1])
            return res[k][1] + 1




food_times = [1,4,2,3,2]
k = 9

print(solution(food_times, k))