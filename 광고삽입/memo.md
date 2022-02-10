### 경주로 건설
link : [광고삽입 kakao 2021](https://programmers.co.kr/learn/courses/30/lessons/72414/)

-----------------------------------

이전에 비슷한 문제를 이진탐색을 이용해 푼 적이 있다.

그 때는 전체 시간초 구간이 너무 길어서 각 초단위로 탐색하는것이 불가능해서

시간을 정렬해놓고 시간 구간의 시작점과 끝지점의 index를 찾는 방법으로 했었다.

같은 방법으로 이번 문제를 풀어보려했는데, 틀린 문제가 있는 건 둘째치고 시간초과가 발생했다.

logs가 많아 각각 log에 이진탐색을 하는것이 더 비효율적이었다.

대신 이번문제는 시간구간이 99:99:99 까지로 약 36만초 정도로 충분히 순회가 가능했다.

그래서 각 시점 마다의 누적 시청시간을 구해서 문제를 풀었다.

    
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

다만 주의할 점은 어떤 시간부터 시청을 시작해도 실제로 1초를 시청하게 되는것은

시청을 시작한 뒤 1초가 지난 시점이므로 시청시간을 더할 때

해당 시간의 1초 뒤 시점에 시청시간을 더해주었다.

그래서 times는 0초와 마지막 시간 +1초를 포함해서

전체 시간구간 +2 만큼의 공간이 필요하다.