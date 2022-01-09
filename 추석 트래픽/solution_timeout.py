import bisect

def solution(lines):
    n = len(lines)
    s_sorted = []
    e_sorted = []

    for l in lines:
        _, ends, t = l.split()
        h, m, s= ends.split(':')
        end = (int(h)*60 + int(m)) *60000 + int(s.replace('.',''))
        t = int(float(t[:-1]) * 1000)
        start = end -t +1

        s_sorted.append(start)
        e_sorted.append(end)
    
    s_sorted.sort()

    check_start = s_sorted[0]
    check_end = check_start + 999
    answer = 1
    while check_end <= e_sorted[-1]:
        s_out = bisect.bisect_left(e_sorted, check_start)
        e_out = n - bisect.bisect_right(s_sorted, check_end)

        max = n - e_out - s_out
        if answer < max:
            answer = max

        check_start +=1; check_end +=1

    return answer



lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

lines =[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
s = solution(lines)
print(s)

# 모든 구간에 대해서 완전탐색.
# 끝 시간 기준정렬.
# 시작시간 기준 정렬.
