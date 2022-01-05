
def solution(user_id, banned_id):
    possible_set_lst = []
    
    for ban in banned_id:
        possible_set = [user for user in user_id if checkid(user, ban)]
        possible_set_lst.append(possible_set)

    res = [[]]
    for possible_set in possible_set_lst:
            res = [x + [y] for x in res for y in possible_set if y not in x ]

    sol = []
    for x in res:
        x = set(x)
        if len(x) == len(banned_id) and x not in sol:
            sol.append(x)

    return len(sol)

def checkid(user, ban):
    if len(user) != len(ban):
        return False

    for i in range(len(user)):
        if ban[i] == '*' or user[i] == ban[i]:
            continue
        else:
            return False

    return True
