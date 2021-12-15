
import copy

def solution(key, lock, rotate_cnt=0):
    
    m = len(key)
    n = len(lock)
    answer = False

    # 패딩이 들어간 lock 생성.
    p = m-1
    p_lock = [[0 for _ in range(n + p*2)] for _ in range(n + p*2)]

    for i in range(n):
        for j in range(n):
            p_lock[i+p][j+p] = lock[i][j]

    # 시작자리 결정
    for s_i in range(n+p):
        for s_j in range(n+p):

            # key를 각 자리에 더함
            test_lock = copy.deepcopy(p_lock)
            for i in range(m):
                for j in range(m):
                    test_lock[i+s_i][j+s_j] += key[i][j]


            ## 판별
            sol = 1
            for i in range(n):
                for j in range(n):
                    sol *= test_lock[i+p][j+p]
                    
            if sol ==1:
                answer = True
                return answer


    if rotate_cnt < 3:
        # key를 90도 돌려서 시도
        answer = solution(rotate(key), lock, rotate_cnt=rotate_cnt+1)

    return answer


def rotate(key):
    return [i[::-1] for i in zip(*key)]



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
         [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))