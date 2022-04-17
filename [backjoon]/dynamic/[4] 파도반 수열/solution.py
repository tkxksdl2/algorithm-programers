def solution(q):
    lib = [1,1,1,2,2]
    ans = []

    for i in q:
        if i <= len(lib):
            ans.append(lib[i-1])
        else:
            for j in range(len(lib), i):
                lib.append(lib[j-1] + lib[j-5])
            ans.append(lib[i-1])
    return ans

n = int(input())
q = [int(input()) for _ in range(n)]

for a in solution(q):
    print(a)