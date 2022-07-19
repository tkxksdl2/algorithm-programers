import bisect
def solution(info, query):
    info_dict = dict()
    answer = []

    for i in info:
        temp = i.split(' ')
        key = temp[:4]
        value = int(temp[4])

        keys = []
        for n in range(5):
            key_temp = make_keys(key, n)
            for k in key_temp:
                keys.append(''.join(k))

        for key in keys:
            if key in info_dict.keys():
                info_dict[key].append(value)
            else:
                info_dict[key] = [value]

    for key in info_dict.keys(): 
        info_dict[key].sort()
        
    query = [x.replace(' and', '').split(' ') for x in query]

    for q in query:
        key = ''.join(q[:4]).replace('-','')
        value = int(q[4])

        if key not in info_dict.keys():
            answer.append(0)
            continue

        ans = len(info_dict[key])- bisect.bisect_left(info_dict[key], value)
        answer.append(ans)

    return answer

def make_keys(arr, n): 
    result =[] 
    if n == 0: 
        return [[]] 
    for i in range(0, len(arr)):
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in make_keys(rest_arr, n-1): 
            result.append([elem]+C) 
            
    return result


info =["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]

print(solution(info, query))