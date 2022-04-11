lib = dict()
def solution():
    lst = []
    while True:
        a, b, c = list(map(int, input().split()))
        if a == b == c == -1:
            break

        lst.append([a,b,c])

    for a, b, c in lst:
        print(f"w({a}, {b}, {c}) = ", recur(a,b,c))


def recur(a,b,c):
    if (a,b,c) in lib:
        return lib[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        v = 1
    elif a > 20 or b > 20 or c > 20:
        v = recur(20,20,20)
    elif a < b and b < c:
        v = recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a, b-1, c)
    else:
        v = recur(a-1,b,c) + recur(a-1, b-1, c) +recur(a-1,b,c-1) - recur(a-1,b-1,c-1)
    lib[(a,b,c)] = v
    return v

solution()