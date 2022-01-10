### 메뉴 리뉴얼
link : [메뉴 리뉴얼 카카오 2021](https://programmers.co.kr/learn/courses/30/lessons/72411)

-----------------------------------

단순히 알파벳들의 조합을 만들고 조건에 맞춰서 검색하는 문제이다.

파이썬의 경우 collections 라이브러리를 이용해 조합을 쉽게 구현할 수 있지만,

이번에는 조합의 작동방식을 알아볼 겸 굳이 구현해보기로 했다.

직접 처음부터 구현하자니 구조가 난감해 아래 블로그의 도음을 받았다.

[블로그](https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)


    def combination(arr, n):
    used = [0 for _ in arr]
    result = []

    def generate(res):
        if len(res) == n:
            result.append(res.copy())
            return

        #처음엔 0, 이후는 끝값 + 1
        start = arr.index(res[-1]) + 1 if res else 0
        for i in range(start, len(arr)): # 시작부터 이후 값 까지 반복.
            # 이전값과의 비교. 즉 중복검사로, arr 가 정렬되있다고 가정할 때 사용함.
            if used[i] == 0 and (i == 0 or arr[i-1] != arr[i] or used[i-1]): 
                res.append(arr[i])
                used[i] = 1 #사용설정
                generate(res)
                res.pop()   # 한 숫자사용 분기가 끝나면 그 숫자를 뻄.
                used[i] = 0
    
    generate([]) # 최초실행.
    return result

따라 코딩하면서 주석을 달고 값을 return할 수 있도록 수정했다.

그 이외에 조건을 검열하는 부분은 딕셔너리를 이용했지만,

다른사람의 풀이를 보니 Counter 객체를 사용하면 더 쉽게 할 수 있었다.