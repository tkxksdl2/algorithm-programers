### 뉴스 클러스터링
link : [뉴스 클러스터링](https://programmers.co.kr/learn/courses/30/lessons/17677)

-----------------------------------

문자열을 검열해 토큰을 세우고 자카드 계수를 구하는 문제.

개인적으로 image sementic segmantation 프로젝트를 해봤었기에

자카드 계수를 직접 사용해본적이 있다. 그래서 어렵지 않게 이해 할 수 있었다.

문자열의 토큰을 만드는 부분 역시 자연어 처리에서 많이 사용되는 부분이어서 익숙했다.

일전에는 이런 문제일 때 라이브러리 사용을 최대한 자제했지만,

이번에는 작정하고 사용해 코드 줄수를 줄이는 데 집중해봤다.

    #토큰을 만드는 부분
    str1 = Counter([(str1[i] + str1[i+1]).lower() for i in range(len(str1)-1) \
                                    if r.match(str1[i]) and r.match(str1[i+1])])
    str2 = Counter([(str2[i] + str2[i+1]).lower() for i in range(len(str2)-1) \
                                    if r.match(str2[i]) and r.match(str2[i+1])])

카운터 객체가 편리한 줄은 알았지만 합집합과 교집합도 쉽게 만들어지는 줄은 몰랐었다.

굉장히 편하다.

    #카운터 객체의 편리함
    intersection = str1 & str2
    union = str1 | str2


하다보니 가독성이 별로인 것 같긴 하지만 코드는 짧아서 만족스럽다.