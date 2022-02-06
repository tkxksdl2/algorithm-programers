# k를 기준으로 순회를 돌면 안됨.
def solution(k, room_number):
    room_dict = dict()
    answer = []

    for n in room_number:
        temp = []
        while n in room_dict:
            temp.append(n)
            n = room_dict[n]
        room_dict[n] = n+1
        for n_temp in temp:
            room_dict[n_temp] = n+1
            
        answer.append(n)

    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))