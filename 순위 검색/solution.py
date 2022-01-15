def solution(info, query):
    answer = []

    info = [i.split(' ')for i in info]
    query = [x.replace(' and', '').split(' ') for x in query]

    for q in query: 
        answer.append(search(info, q))

    return answer

def search(info, q):
    temp = info
    for i in range(len(q)):
        if q[i] == '-':
            continue
        
        nxt = []

        if i < 4:
            temp.sort(key = lambda x : (x[i])) 

            for t in temp:
                if t[i] == q[i]: nxt.append(t)

        else : 
            temp.sort(key = lambda x : int(x[i])) 

            for t_i, t in enumerate(temp):
                if int(t[i])>= int(q[i]): 
                    nxt = temp[t_i:]
                    break
                
        temp = nxt
        
    return len(temp)

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

print(solution(info,query))