def solution(s):
    s = [ set(map(int, n.split(','))) for n in s[2:-2].split('},{')]
    s.sort(key = lambda i:len(i))
    answer = []

    present = set() 
    for next in s:
        answer.append((next-present).pop())
        present = next

    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(s))

