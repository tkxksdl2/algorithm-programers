from collections import deque
import itertools

def solution(n, weak, dist):
    dist.sort(reverse=True)

    for i in range(len(dist)):
        weak_res = deque(weak)
        using_dist = list(map(list,itertools.permutations(dist[:i+1])))

        for p in using_dist:
            for w_i in range(len(weak_res)): # 시작점 선택
                weak_res_copy = weak_res.copy()
                p_copy = p.copy()
                for _ in range(w_i): # 덱 회전
                    weak_res_copy.append(weak_res_copy.popleft() + n)
                
                while p_copy and weak_res_copy:
                    startpoint = weak_res_copy.popleft() + p_copy.pop(0)
                    while len(weak_res_copy) > 0 and startpoint >= weak_res_copy[0]:
                        weak_res_copy.popleft()

                    if len(weak_res_copy) ==0:
                        return i + 1

    return -1


n, weak, dist = (200, [0, 10, 50, 80, 120, 160],[1, 5, 10, 30,40])


sol = solution(n, weak, dist)
print(sol)