from tracemalloc import start


def solution(food_times, k):
    if k > sum(food_times):
        return -1
    
    linked_dict = dict()
    for idx, time in enumerate(food_times):
        linked_dict[idx] = {'value':time,'pre':(idx-1)%len(food_times), 'nxt': (idx+1)%len(food_times)}
    
    len_dict = len(linked_dict)
    start_point = 0
    while True:
        min = 100000001
        while linked_dict[start_point]['value'] == 0:
            start_point = linked_dict[start_point]['nxt']

        current = start_point
        while True:
            if linked_dict[current]['value'] < min: 
                min = linked_dict[current]['value']
            if linked_dict[current]['nxt'] < current:
                break
            current = linked_dict[current]['nxt']
            

        if min * len_dict < k:
            k -= min * len_dict
            current = start_point
            while True:
                linked_dict[current]['value'] -= min

                if linked_dict[current]['value'] == 0:
                    linked_dict[linked_dict[current]['pre']]['nxt'] = linked_dict[current]['nxt']
                    linked_dict[linked_dict[current]['nxt']]['pre'] = linked_dict[current]['pre']
                    len_dict -= 1
                current = linked_dict[current]['nxt']
                if linked_dict[current]['nxt'] < current:
                    break

        else: break
            


    idx = start_point
    while k > 0:
        linked_dict[idx]['value'] -= 1
        
        if linked_dict[idx]['value'] == 0:
            linked_dict[linked_dict[idx]['pre']]['nxt'] = linked_dict[idx]['nxt']
            linked_dict[linked_dict[idx]['nxt']]['pre'] = linked_dict[idx]['pre']
        
        idx = linked_dict[idx]['nxt']
        k -=1
        
    return idx+1

food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))
