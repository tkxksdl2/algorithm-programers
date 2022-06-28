def balance(s):
    stack = [0]
    for d in s:
        if d == '[':
            stack.append('[')
        elif d == '(':
            stack.append('(')
        elif d == ']':
            if stack.pop() != '[':
                return 'no'
        elif d == ')':
            if stack.pop() != '(':
                return 'no'
    
    if len(stack) > 1: return 'no'
    return 'yes'

while True:
    s = input()
    if s == '.': break
    print(balance(s))