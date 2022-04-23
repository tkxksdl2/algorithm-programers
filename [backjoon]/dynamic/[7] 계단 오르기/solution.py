def solution(n, stair):
    if n == 1:
        return stair[0]

    arr = [0 for _ in range(301)]
    arr1 = [0 for _ in range(301)]
    
    arr[0] = stair[0]; arr[1] = stair[0] + stair[1]
    arr1[1] = stair[1]
    
    for i in range(2, len(stair)):
        arr[i] = stair[i] + max(arr[i-2], arr1[i-1])
        arr1[i] = stair[i] + arr[i-2]

    return arr[n-1]

n = int(input())
stair = [int(input()) for _ in range(n)]
print(solution(n, stair))

# arr는 특정 칸을 밟았을 경우 최대값을 저장한다.
# 경우의 수는 두가지인데, 두칸 전을 밟았을 경우와
# 한칸 전을 밟았는데, 그 이전에 두칸 전을 밟았을 경우이다.
# 떄문에 한칸 전을 밟을 경우를 보기 위해선 무조건 최대값을 보는 게 아니라
# 한칸 전 타일을 밟았을 때 두칸 전 타일을 밟았을 경우를 보아야 한다.
# 때문에 무조건 두칸 전 타일을 밟았을 경우만을 저장하는 arr1을 만든다.
# 현재 칸을 밟았을 경우는, arr의 2인덱스 전과 arr1의 1인덱스 전 값중 최대값을 더하는 경우이다.