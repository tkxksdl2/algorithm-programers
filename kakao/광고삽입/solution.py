def solution(play_time, adv_time, logs):
    play_time = time2int(play_time)
    adv_time = time2int(adv_time)

    logs = [list(map(time2int ,log.split('-'))) for log in logs]
    times = [0 for _ in range(play_time+2)]
    answer = {'value':0, 'time':0}

    for start,end in logs:
        times[start+1] += 1
        times[end+1] -= 1

    for i in range(1, len(times)):
        times[i] += times[i-1]
    for i in range(1, len(times)):
        times[i] += times[i-1]
    for i in range(play_time-adv_time+1):
        time_accumul = times[i+adv_time] - times[i]
        if answer["value"] < time_accumul:
            answer['value'] = time_accumul
            answer['time'] = i
    
    
    m,s = divmod(answer['time'], 60)
    h,m = divmod(m, 60)
    
    return ':'.join([int2time(h), int2time(m), int2time(s)])


def time2int(time):
    h, m, s = map(int,time.split(':'))
    return s + (m + h*60) * 60

def int2time(i):
    if i<10:
        return '0'+str(i)
    return str(i)

    
play_time = "00:00:08"
adv_time = "00:00:03"
logs = ["00:00:00-00:00:08", "00:00:05-00:00:08"]
print(solution(play_time, adv_time ,logs))