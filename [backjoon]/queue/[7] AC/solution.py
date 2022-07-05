for _ in range(int(input())):
    proc = input()
    n = int(input())

    temp = input().strip('[').strip(']')
    lst = list(temp.split(',')) if temp else []

    f = 0; b = n-1
    toggle = 0

    for p in proc:
        if p == 'R':
            toggle = 0 if toggle else 1
        else:
            if not toggle:
                f += 1
            else:
                b -= 1
            
    
    if b - f < -1:
        print('error')
    elif not toggle:
        print('['+ ','.join(lst[f:b+1]) + ']')
    else:
        print('['+ ','.join(lst[f:b+1][::-1]) + ']')