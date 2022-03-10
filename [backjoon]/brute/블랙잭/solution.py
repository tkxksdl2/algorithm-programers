def solution(n,m, cards):
    ans_lst =[]
    permutation(cards, [], ans_lst)
    ans_lst = [sum(x) if sum(x) <= m else 0 for x in ans_lst]
    
    return max(ans_lst)

def permutation(arr,res, ans, k=3):
    if k == 1:
        
        for i in range(len(arr)):
            ans.append(res + [arr[i]])
        return

    for i in range(len(arr)-k+1):
        permutation(arr[i+1:], res+[arr[i]], ans,  k-1)

    
n, m = map(int, input().split())
cards = list(map(int, input().split()))

solution(n,m,cards)