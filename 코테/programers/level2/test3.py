import math
def solution(fees, records):
    answer = []
    bills = {}
    for i in range(len(records)):
        time, num, state = records[i].split()
        h, m = map(int, time.split(':'))
        time = 60 * h + m
        num = int(num)
        
        if num not in bills:
            bills[num] = [state, time, 0]
        else:
            if state == "IN":
                bills[num][0] = "IN"
            else:
                bills[num][0] = "OUT"
                bills[num][2] += (time - bills[num][1])
            bills[num][1] = time
        
    for num in sorted(list(bills.keys())):
        if bills[num][0] == "IN":
            bills[num][2] += ((23*60+59) - bills[num][1])

        if bills[num][2] > fees[0]:
            answer.append(fees[1] + math.ceil((bills[num][2] - fees[0]) / fees[2]) * fees[3] )
        else:
            answer.append(fees[1])

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN"
            , "06:00 0000 IN"
            , "06:34 0000 OUT"
            , "07:59 5961 OUT"
            , "07:59 0148 IN"
            , "18:59 0000 IN"
            , "19:09 0148 OUT"
            , "22:59 5961 IN"
            , "23:00 5961 OUT"]

print(solution(fees, records))