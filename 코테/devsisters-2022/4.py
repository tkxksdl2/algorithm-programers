def solution(L):
    answer = []
    i = 0
    L_dict = {}
    for l in L:
        if l[1] in L_dict:
            L_dict[l[1]].append(l)
        else: 
            L_dict[l[1]] = [l]
    answer = sorted(L_dict[0])

    n = 1
    while len(answer) < len(L):
        if n not in L_dict:
            n += 1; continue
        adding_list = L_dict[n]
        adding_list.sort()
        
        while adding_list:
            cnt = 0
            temp = adding_list.pop()

            for i in range(len(answer)):
                if answer[i][0] >= temp[0]:
                    cnt += 1

                if cnt == n:
                    answer.insert(i+1, temp)
                    break
            
        n += 1

    return answer


L = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = solution(L)
print( s)