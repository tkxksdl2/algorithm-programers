### 수식 최대화
link : [수식 최대화 2020카카오](https://programmers.co.kr/learn/courses/30/lessons/67257/)

-----------------------------------

문자열로 된 수식을 차례대로 연산하는 문제.

순열과 정규 표현식을 적극적으로 이용해 구현해보았다.

단 식의 중간과정이 음수가 되었을 때 이를 조절하는데 약간 애를 먹었다.

그래서 음수일 때 괄호를 씌워서 이를 다시 정규표현식으로 찾아내는 추가 과정이 필요했다.

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


특히 괄호를 찾을 때 음수 부호가 -연산자와 혼동되는 것을 막기 위해

'(-'를 한꺼번에 찾아야 했는데, 이 때 정규표현식에 익숙하지 않아서 애를 먹었다.

괄호는 \\(로 표현해야 하지만 -의 경우는 대괄호 안에 있는 게 아니라면 굳이 \\-로 표현할 필요가 없었다.

그래서 '(-'를 찾는 표현은 다음과 같다.

    (\(-)?

이 부분에서 많은 시간이 잡아먹힌게 아쉬울 따름이다.