def solution(new_id):
    new_id = new_id.lower()
    print(new_id)

    new_id = [a for a in new_id if (ord(a)>=97 and ord(a) <= 122) or 
                                    (ord(a)>=48 and ord(a) <= 57) or
                                    ord(a) == 45 or ord(a) == 95 or ord(a) ==46]
    new_id = ''.join(new_id)
    print(new_id)

    while True:
        if '..'in new_id:
            new_id = new_id.replace('..', '.')
        else: break
    
    print(new_id)

    new_id = new_id.strip('.')
    print(new_id)

    if not new_id:
        new_id = 'a'
    print(new_id)

    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
    print(new_id)

    if len(new_id) <=2:
        while len(new_id)<3:
            new_id += new_id[-1]
    
    print(new_id)


    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"

s = solution("100101004010")

print(ord('0'))