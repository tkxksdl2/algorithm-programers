def hanoi(n, start, dest, extra, info):
    if n == 1:
        info['res'].append([start, dest])
        info['cnt'] +=1
        return

    hanoi(n-1, start, extra, dest, info)
    info['res'].append([start, dest])
    info['cnt'] +=1
    hanoi(n-1, extra, dest, start, info)


info = {'cnt':0, 'res':[]}
hanoi(int(input()), 1, 3, 2, info )
print(info['cnt'])
for step in info['res']:
    print(step[0], step[1])