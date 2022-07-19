import bisect

def solution(lines):
    n = len(lines)
    s_sorted = []
    e_sorted = []

    for l in lines:
        _, ends, t = l.split()
        h, m, s= ends.split(':')
        end = (int(h)*60 + int(m)) * 60000 + int(s.replace('.',''))
        t = int(float(t[:-1]) * 1000)
        start = end -t +1

        s_sorted.append(start)
        e_sorted.append(end)
    
    s_sorted.sort()
    
    answer =1
    for check_start in e_sorted:
        check_end = check_start + 999
        s_out = bisect.bisect_left(e_sorted, check_start)
        e_out = bisect.bisect_right(s_sorted, check_end)

        max = e_out - s_out
        if answer < max:
            answer = max

        check_start +=1; check_end +=1

    return answer

