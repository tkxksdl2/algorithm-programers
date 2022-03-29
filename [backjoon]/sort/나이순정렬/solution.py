import sys
def solution(n):
    age_dict = dict()
    for _ in range(n):
        age, name = sys.stdin.readline().strip().split()
        if int(age) not in age_dict:
            age_dict[int(age)] = [name]
        else:
            age_dict[int(age)].append(name)
    for age in range(1, 201):
        if age in age_dict:
            for name in age_dict[age]:
                print(age, name)


n = int(sys.stdin.readline())
solution(n)
