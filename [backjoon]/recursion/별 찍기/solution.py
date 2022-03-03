def solution(n, base=[['*']]):
    head = [row * 3 for row in base]
    body = [row + [' ']*len(row) + row for row in base]

    res = head + body + head

    if n==3: 
        for row in res:
            print(''.join(row))
        return

    solution(n/3, res)

    
solution(int(input()))
