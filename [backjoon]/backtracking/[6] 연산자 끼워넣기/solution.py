def solution(n, nums, cals):
    global maxval, minval
    
    maxmin = [-(10**9) -1, 10**9 + 1]
    
    
    

    def dfs(step, preval, maxmin):
        if step == n:
            if preval > maxmin[0]: maxmin[0] = preval
            if preval < maxmin[1]: maxmin[1] = preval
            return

        for c in range(4):
            if cals[c]:
                cals[c] -= 1

                if c == 0:
                    dfs(step+1, preval + nums[step], maxmin)
                elif c == 1:
                    dfs(step+1, preval - nums[step], maxmin)
                elif c == 2:
                    dfs(step+1, preval * nums[step], maxmin)
                else:
                    if preval < 0 and nums[step] > 0:
                        dfs(step+1, -( -preval // nums[step]), maxmin)
                    else:
                        dfs(step+1, preval // nums[step], maxmin)
                
                cals[c] += 1
                    
        return

    dfs(1, nums[0], maxmin)

    print(maxmin[0])
    print(maxmin[1])



n = int(input())
nums = list(map(int, input().split())) 
cals = list(map(int, input().split())) 
solution(n, nums, cals)