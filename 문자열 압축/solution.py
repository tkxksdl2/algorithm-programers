import sys
import math
sys.setrecursionlimit(1000000)

def solution(s):
    len_s = len(s)
    count_list = [len_s] # 최대 길이
    
    token_list = [i+1 for i in range(int(len_s/2))] # 절반 길이까지 확인한다.
    
    
    for len_token in token_list:
        count_list.append(get_count(s, len_token, start_idx=0))

    print(count_list)
    
    return min(count_list)


def get_count(s, len_token, start_idx=0, repeat_count=0):
    end_idx = start_idx + len_token # 끝 idx
    
    if (end_idx > len(s)) and (repeat_count > 0):
        return len(s[start_idx:]) + int(math.log10(repeat_count + 1) +1) #반복중에 탈출하면 쌓여있던 반복의 자릿수를 더함.
    elif (end_idx > len(s)) and (repeat_count == 0):
        return len(s[start_idx:])
        
    next_token = s[end_idx: end_idx + len_token ] # 다음 단위
    token = s[start_idx : end_idx] # 반복을 확인할 단위
    
    
    if (token == next_token): # 이후가 반복됨
             
        if (repeat_count > 0):              # 이미 반복중일 때, repeat_count만 쌓임.
            return get_count(s, len_token, start_idx=end_idx, repeat_count = repeat_count + 1)
        
        elif ( repeat_count == 0):          #처음으로 반복이 시작될 때 + token 길이
            return len_token + get_count(s, len_token, start_idx=end_idx, repeat_count = repeat_count + 1)
    
    elif (token != next_token): # 반복이 중단됨.
        
        if (repeat_count == 0):              # 전에 반복되지 않았고 다음 반복도 없으면 + token 길이
            return  len_token + get_count(s, len_token, start_idx=end_idx, repeat_count=0)
        
        elif ( repeat_count > 0):            # 반복되는 중에 반복이 끝나면 쌓여있던 반복의 자릿수를 더함.
            return int(math.log10(repeat_count + 1) +1) + get_count(s, len_token, start_idx=end_idx, repeat_count=0) 
    
solution('aabbaccc')
