def solution(n,t,m,timetable):
    bustime = dict()
    basictime = '09:00'
    timetable.sort()

    for bus_i in range(n):
        bustime[addtime(basictime, t*bus_i)] = []

    for time in timetable:
        for key in bustime.keys():
            if time <= key and len(bustime[key]) < m:
                bustime[key].append(time)
                break

    last_key =list(bustime.keys())[-1]

    if len(bustime[last_key]) < m:
        return last_key

    return addtime(bustime[last_key][-1], -1)

def addtime(time, delta):
    h, m = map(int, time.split(':'))
    m += delta
    h += m // 60
    m %= 60
    
    h = str(h) if h>=10 else '0'+ str(h)
    m = str(m) if m>=10 else '0'+ str(m)

    return h + ':' + m 


n = 10
t = 2
m = 2
timetable = ["09:10", "09:09", "08:00", '09:18','09:18']
print(solution(n,t,m,timetable))

