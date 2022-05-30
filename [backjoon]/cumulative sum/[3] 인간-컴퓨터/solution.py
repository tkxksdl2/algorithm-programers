import sys
def solution(sentence, q):
    acc = [[0] for _ in range(26)]
    acc[ord(sentence[0])-97][0] = 1

    for i in range(1, len(sentence)):
        for j in range(26):
            if chr(j+97) == sentence[i]:
                acc[j].append(acc[j][i-1] + 1)
            else:
                acc[j].append(acc[j][i-1])
    
    for i in range(q):
        w, s, e = sys.stdin.readline().split()
        s = int(s); e = int(e)
        if not s:
            sys.stdout.write(str(acc[ord(w)-97][e]) + '\n')
        else:
            sys.stdout.write(str(acc[ord(w)-97][e] - acc[ord(w)-97][s-1]) + '\n')

sentence = sys.stdin.readline()
q = int(sys.stdin.readline())
solution(sentence, q)