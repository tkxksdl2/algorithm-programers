def solution(n ,k ,cmd):
    initial_list = [i for i in range(n)]
    answer = ['O'for _ in range(n)]
    deleted_list =[]

    for command in cmd:
        if command[0] in ['D', 'U']:
            if command[0] =='D': k += int(command[2:])
            else:                k -= int(command[2:])
            
        elif command[0] == 'C':
            deleted_list.append((initial_list.pop(k), k))
            if k == len(initial_list):
                k -= 1
                
        else:
            value , index = deleted_list.pop()
            initial_list.insert(index, value)
            if index <= k:
                k += 1
        print(command, k, '\n',initial_list)
    print(deleted_list)
    for value, _ in deleted_list: answer[value] = 'X'
    return ''.join(answer)


n, k = 8,2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k, cmd))
