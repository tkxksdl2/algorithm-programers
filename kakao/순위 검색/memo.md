### 순위 검색
link : [순위 검색 2021 카카오](https://programmers.co.kr/learn/courses/30/lessons/72412/)

-----------------------------------

데이터셋을 다중의 조건을 넣어 검색하는 문제.

일반적인 데이터셋의 query의 검색기능과 유사해

그런 기능을 구현하는 문제인가 했지만,

효율성 문제에서 걸려버렸다.

효율성에 걸릴 것을 예상하고 일단 짠 코드는 solution.py에 있다.

이 코드는 일반적인 선형 탐색으로 구현되어 있다.

또, 검색하려는 조건 마다 나머지 리스트를 정렬하기 때문에,

많은 시간이 걸리는 것은 뻔했다.

-------------------------------------------

효율성을 어떻게 끌어올릴 지를 계속 생각했지만 

혼자서는 아이디어를 생각해내기 힘들었다.

결국 카카오 풀이의 도움을 얻었는데,

답은 검색에 걸릴수 있는 모든 조건을 해쉬값으로 때려박는 것이다.

단순무식하지만 확실한 방법이다. 다만 이방법은 조건의 경우의 수가 적기에 가능한 일이다.

데이터 하나 당 검색이 되는 query 경우의 수는 2 * 2 * 2 * 2 = 16 뿐이다.

그래서 데이터 하나 당 16가지의 key로 데이터를 추가하면 된다.

저장효율도 나쁘고 여러모로 억지라는 느낌도 들지만

어쨌던 효율성은 통과한다.

        keys = []
            for n in range(5):
                key_temp = make_keys(key, n)
                for k in key_temp:
                    keys.append(''.join(k))

            for key in keys:
                if key in info_dict.keys():
                    info_dict[key].append(value)
                else:
                    info_dict[key] = [value]

    ------------------------------------------
    def make_keys(arr, n): 
        result =[] 
        if n == 0: 
            return [[]] 
        for i in range(0, len(arr)):
            elem = arr[i] 
            rest_arr = arr[i + 1:] 
            for C in make_keys(rest_arr, n-1): 
                result.append([elem]+C) 
                
        return result

조건들을 조합을 통해 어떤 것을 선택하고 선택하지 않을지를 골라 16가지를 만든다.

그리고 조건을 key로 정하고 점수 int를 값으로 넣는다.

남은 일은 점수를 정렬하고 이진탐색으로 개수를 검색하는 일 뿐이다.

이 코드는 solution2.py에 저장되어있다.

2단계 문제 치고는 까다로웠던 것 같다.