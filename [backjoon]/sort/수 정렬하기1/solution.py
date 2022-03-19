def selection(lst):
    for i in range(len(lst)):
        min_v = float('inf')
        min_idx = int()
        for j in range(i, len(lst)):
            if lst[j] < min_v:
                min_v = lst[j] 
                min_idx = j
        lst[min_idx] = lst[i]
        lst[i] = min_v

    return lst

def insertion(lst):
    for i in range(1, len(lst)):
        target = lst[i]
        for j in range(i-1, -1, -1):
            if target < lst[j]:
                lst[j+1] = lst[j]
                lst[j] = target
    
    return lst

def bubble(lst):
    for i in range(len(lst)-1, -1, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
            
    return lst

n = int(input())
lst = [int(input()) for _ in range(n)]

# print(selection(lst))
# print(insertion(lst))
print(bubble(lst))