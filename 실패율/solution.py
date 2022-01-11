def solution(N, stages):
    failures = []
    players_n = len(stages)

    for i in range(1, N+1):
        if players_n == 0:
            failures.append([0, i])
            continue

        fail_n = stages.count(i)
        failures.append([fail_n/players_n, i])
        players_n -= fail_n

    answer = [x[1] for x in sorted(failures, key = lambda x: (-x[0],x[1]))]
                
    return answer

N = 5
stages = [1,2,3,3,3,3]	

print(solution(N, stages))