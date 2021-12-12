
# def solution(p):
#     answer = ''
#     return 

def solution(p):
    if p == '':
        return ""
    
    
    balance = 0
    for idx, word in enumerate(p):
        if word == '(':
           balance += 1
        elif word == ')':
            balance -= 1
        
        if balance == 0:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    
    #올바른 문자열은 무조건 앞이 '(' 이어야한다.
    
    if u[0] == ')':
        temp = ''
        for w in u[1:-1]:
            if w == ')':
                temp += '('
            else:
                temp += ')'
                
        return  '(' + solution(v) + ')' + temp
                
        
    
    return u + solution(v)

u = solution('()))((()')
print(u)
