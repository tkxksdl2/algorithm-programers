def solution(openA, closeB):
    endtime = closeB[-1]
    a, b = 0,0
    open = False
    answer = 0
    for t in  range(1, endtime+1):
        if a < len(openA) and openA[a] == t:
            open = True
            a += 1
        elif b < len(closeB) and closeB[b] == t:
            open = False
            b += 1
        
        if open: 
            answer += 1
    
    return answer

openA =[4, 7, 9, 16]
closeB = [2, 5, 12, 14, 20]
print(solution(openA, closeB))