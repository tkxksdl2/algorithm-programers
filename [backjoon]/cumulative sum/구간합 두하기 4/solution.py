def solution(n, m, nums, q):
    for i in range(1,n):
        nums[i] += nums[i-1]

    for s,e in q:
        if s == 1: print( nums[e-1])
        else:
            print(nums[e-1] - nums[s-2])
    return

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
q = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, nums, q)