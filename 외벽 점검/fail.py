def solution(n, weak, dist, dist_cnt=0):
    if not weak:
        print('탈출조건 4')
        return dist_cnt
    if dist_cnt == len(dist):
        print('탈출조건 3')
        return -1

    weak_diff =[]

    for i in range(len(weak) - 1):
        weak_diff.append(weak[i+1] - weak[i])
    weak_diff.append((n - weak[-1] + weak[0]) % n )

    # 지금 최대 긴 예외를 제한 부분이 dist중 가장 큰 부분보다 크다면
    # 예외의 단위를 늘려야 한다.

    print(weak_diff)
    weak_diff_cnt = 1
    weak_len = len(weak)
    next_weak_diff = weak_diff.copy()
    while True:
        print()
        print('현재 max diff = ', max(next_weak_diff))
        print('현재 분절 = ', n - max(next_weak_diff))
        print('현재사용하는 dist = ', dist[-1 - dist_cnt])
        if weak_diff_cnt > weak_len: # 더 이상 줄일수도 없고 더 큰 dist도 없음. 즉 현재부턴 모든 dist가 한개만을 확인가능
            if len(dist) - dist_cnt >= weak_len: # 그런데 남아있는 dist가 많으면
                print('탈출조건 1')
                return dist_cnt + weak_len
            else:                               # dist가 부족하면.
                print('탈출조건 0')
                return -1

        if n - max(next_weak_diff) > dist[-1 - dist_cnt]:
            
            next_weak_diff = [next_weak_diff[i] + weak_diff[(i+weak_diff_cnt) % weak_len]  for i in range(weak_len) ]
            weak_diff_cnt += 1
            print('최대 줄어듦, weak_diff_cnt = ', weak_diff_cnt)
            
            
            print(next_weak_diff)
        else:
            print('탈출')
            weak_diff = next_weak_diff
            break
    

    print('작업의 시작과 끝지점.') # 예외와는 반대임.


    end_idx = weak_diff.index(max(weak_diff)) 
    start_idx = (end_idx + weak_diff_cnt) % weak_len

    print(start_idx, end_idx)
    print('weak_diff_cnt = ',weak_diff_cnt)

    remove_list = []
    for _ in range(weak_len - weak_diff_cnt + 1):
        remove_list.append(weak[start_idx])
        start_idx = (start_idx + 1) % weak_len
    
    for d in remove_list:
        weak.remove(d)

    print('줄어든 결과 weak',weak)

    return solution(n, weak, dist, dist_cnt=dist_cnt+1)


n, weak, dist = (200, [0, 10, 50, 80, 120, 160],[1, 5, 10, 30,40])
#n, weak, dist = (12, [1,3,4,9,10], [3,5,7])

sol = solution(n, weak, dist)
print(sol)