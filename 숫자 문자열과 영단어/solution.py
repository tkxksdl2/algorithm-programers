def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for e in eng:
        s = s.replace(e, str(eng.index(e)))
    
    return int(s)
s = "one4seveneight"
s = solution(s)
print(s)
