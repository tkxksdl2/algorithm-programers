def solution(play_time, adv_time, logs):
    play_time = time2int(play_time)
    adv_time = time2int(adv_time)

    logs = [list(map(time2int ,log.split('-'))) for log in logs]
    logs.sort()
    logs_e = sorted(logs, key=lambda x:x[1])
    
    answer = 0
    temp = 0
    for start_idx, log in enumerate(logs):
        start, _ = log

        if start > play_time - adv_time:
            start = play_time - adv_time
        
        adv_endtime = start + adv_time
        end_idx = bisect_endtime(adv_endtime, logs)
        
        checking_block = logs[start_idx: end_idx]
        timesum = 0
        for s,e in checking_block:
            if e >= adv_endtime:
                e = adv_endtime
            timesum += e-s

        start_idx = bisect_endtime(start, logs_e, flag=1)
        end_idx = bisect_endtime(adv_endtime, logs_e, flag=1)
        checking_block = logs_e[start_idx: end_idx]

        for s,e in checking_block:
            if s >= start: continue
            timesum += e -start

        if timesum > temp:
            temp = timesum
            answer = start
        
        if start == play_time-adv_time: break

    m,s = divmod(answer, 60)
    h,m = divmod(m, 60)
    
    return ':'.join([int2time(h), int2time(m), int2time(s)])

def bisect_endtime(endtime, logs, flag=0):
    s_idx = 0
    e_idx = len(logs)
    if flag == 0:
        while e_idx - s_idx > 0:
            m_idx = s_idx + (e_idx - s_idx) // 2    
            if logs[m_idx][flag] > endtime:
                e_idx = m_idx
            else:
                s_idx = m_idx+1
    else:
        while e_idx - s_idx > 0:
            m_idx = s_idx + (e_idx - s_idx) // 2    
            if logs[m_idx][flag] >= endtime:
                e_idx = m_idx
            else:
                s_idx = m_idx+1
        
    return e_idx


def time2int(time):
    h, m, s = map(int,time.split(':'))
    return s + (m + h*60) * 60

def int2time(i):
    if i<10:
        return '0'+str(i)
    return str(i)

    
play_time = "02:03:55"
adv_time = "00:14:15"
logs = 	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time ,logs))