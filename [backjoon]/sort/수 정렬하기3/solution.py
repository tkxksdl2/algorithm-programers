import sys
MAX_NUM = 10001

def counting(n):
    counting = [0] * MAX_NUM
    for i in range(n):
        counting[int(sys.stdin.readline())] += 1

    for i, count in enumerate(counting):
        for _ in range(count):
            print(i)

    # for i in range(1, len(counting)):
    #     counting[i] = counting[i-1] + counting[i]
    # res = [None] * n

    # for num in lst:
    #     res[counting[num]-1] = num
    #     counting[num] -= 1

    # for num in res:
    #     print(num)

n = int(sys.stdin.readline())
counting(n)
