def solution(record):
    user_db = dict()
    answer = []

    while record:
        r = record.pop(0).split()
        if r[0] =='Leave':
            command, id = r
        else:
            command, id, nick = r

            if id not in user_db.keys():
                user_db[id] = user(id, nick)
            else:
                user_db[id].nick = nick
        
        if command != 'Change':
            answer.append([command,user_db[id]])

    answer = [u.nick+'님이 들어왔습니다.' if c == 'Enter' else 
                u.nick + '님이 나갔습니다.' for c, u, in answer]
    
    return answer

class user():
    def __init__(self, id, nick):
        self.id = id
        self.nick = nick


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

s = solution(record)
print(s)