import sys

def tim_sort(n,lst):
    min_run = 32

    def insertion(lst, s, e):
        for i in range(s+1, e):
            target = lst[i]
            j = i-1

            # 범위내, y가 더 크거나 같은 경우
            while j >= s and lst[j][1] >= target[1]: 
                if lst[j][1] == target[1]: # y가 같은경우
                    if lst[j][0] > target[0]: # x가 더 큰경우
                        lst[j+1] = lst[j]
                        j -= 1
                    else: # y는 같지만 x가 더 작은경우
                        break
                else: # y 가 더 큰경우
                    lst[j+1] = lst[j]
                    j -= 1
            # y가 더 작거나, y는 같은데 x가 더 작은경우나, 범위끝일때
            lst[j+1] = target
        return lst
    
    def merge(lst, s, m, e):
        res = []
        i, j = s, m
        while i < m and j < e:
            if lst[i][1] == lst[j][1]:
                if lst[i][0] <= lst[j][0]:
                    res += [lst[i]]; i += 1
                else:
                    res += [lst[j]]; j += 1
            elif lst[i][1] < lst[j][1]:
                    res += [lst[i]]; i += 1
            else:
                res += [lst[j]]; j += 1

        while i < m: res += [lst[i]]; i+=1
        while j < e: res += [lst[j]]; j+=1

        for v in res:
            lst[s] = v; s += 1

        return lst 


    for i in range(0, n, min_run):
        insertion(lst, i, min((i+min_run), n))
    
    size = min_run
    # size = 현재 merge할 단위 리스트의 크기.
    # size는 매번 2배가 되기 때문에 size가 n보다 작을동안만 merge 유효
    while size < n:
        for s in range(0, n , size *2):
            
            m = s + size
            if m > n: break; 

            e = min((s + size*2, n))

            merge(lst, s, m, e)

        size *= 2
    
    return lst


n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tim_sort(n, lst)
for a, b in lst:
    print(a, b)