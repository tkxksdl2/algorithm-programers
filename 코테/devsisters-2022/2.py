def solution(join_date, resign_date, holidays):
    answer = 0

    temp, day = join_date.split()
    days_index = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = days_index.index(day)
    
    jy,jm,jd = map(int, temp.split('/'))
    ry,rm,rd = map(int, resign_date.split('/'))

    holidays = set(holidays)
    
    while True:
        sm = str(jm) if jm >= 10 else '0' + str(jm)
        sd = str(jd) if jd >= 10 else '0' + str(jd)

        str_day = sm + '/' + sd

        if str_day not in holidays and day < 5:
            answer += 1

        if jy == ry and jm == rm and jd == rd:
            return answer

        jy, jm, jd, day = nextDay(jy, jm, jd, day)


def nextDay(y,m,d, day):
    month_ends = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #윤년
    if  y % 400 == 0 or (y % 4 ==0 and y % 100 != 0):
        month_ends[1] = 29

    month_end = month_ends[m - 1]

    d += 1
    if d > month_end:
        d = 1; m += 1
        if m > 12:
            m = 1; y += 1

    day = (day + 1) % 7

    return y, m, d, day



join_date = '2019/12/01 SUN'
resign_date = '2020/03/02'
holidays = ["01/02", "12/24", "03/01"]
s = solution(join_date, resign_date, holidays)

print(s)