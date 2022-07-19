from itertools import permutations
import re

def solution(expression):
    answer = 0

    operators = [x for x in ['+', '-','*'] if x in expression]
    operators = list(permutations(operators))

    for operator in operators:
        ex_copy = expression
        for o in operator:
            r = re.compile("(\(-)?\d+\)?\\" + o + "(\(-)?\d+\)?")

            while True:
                m = r.search(ex_copy) 
                if not m: break
                arithmetic = m.group()
                nxt = str(eval(arithmetic)) if eval(arithmetic) >=0 else '('+str(eval(arithmetic)) +')'
                ex_copy = ex_copy.replace(arithmetic, nxt)

        ex_copy = ex_copy.strip('()')
        result = abs(int(ex_copy)) 

        if  result >= answer:
            answer = result

    return answer

expression = "100-200*300-500+20"
s = solution(expression)
print(s)
