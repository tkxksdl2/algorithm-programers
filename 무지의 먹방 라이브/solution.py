def solution(food_times, k):
    if k > sum(food_times):
        return -1
    
    linked_dict = dict()
    for idx, time in enumerate(food_times):
        linked_dict[idx] = {'value':time,'pre':(idx-1)%len(food_times), 'nxt': (idx+1)%len(food_times)}
    
    idx = 0
    while k > 0:
        linked_dict[idx]['value'] -= 1
        
        if linked_dict[idx]['value'] == 0:
            linked_dict[linked_dict[idx]['pre']]['nxt'] = linked_dict[idx]['nxt']
            linked_dict[linked_dict[idx]['nxt']]['pre'] = linked_dict[idx]['pre']
        
        idx = linked_dict[idx]['nxt']
        k -=1
        
    return idx+1
