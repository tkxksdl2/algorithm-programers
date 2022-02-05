# k를 기준으로 순회를 돌면 안됨.
def solution(k, room_number):
    room_dict = dict()
    answer = []
    for n in room_number:
        
        if n in room_dict:
            n = room_dict[n]['next'][0]

        room_dict[n] = {'next' : [n+1, n], 'pre' : [n-1, n]}
        answer.append(n)
        
        if n+1 in room_dict and n-1 in room_dict:
            print('양쪽')
            room_dict[n]['next'] = room_dict[n+1]['next']
            room_dict[n]['pre'] = room_dict[n-1]['pre']
            room_dict[n-1]['next'] = room_dict[n+1]['next']
            room_dict[n+1]['pre'] = room_dict[n-1]['pre']

        elif n+1 in room_dict:
            room_dict[n]['next'] = room_dict[n+1]['next']
            room_dict[n]['pre'] = room_dict[n+1]['pre'] # 객체할당
            room_dict[n]['pre'][0] = n-1

        elif n-1 in room_dict:
            room_dict[n]['pre'] = room_dict[n-1]['pre']
            room_dict[n]['next'] = room_dict[n-1]['next']
            room_dict[n]['next'][0] = n+1
        print(room_dict)
    


    return answer

k = 10
room_number = [3,1,5,4,2]
print(solution(k, room_number))