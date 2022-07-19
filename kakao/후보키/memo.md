### 후보 키
link : [후보 키 카카오 2019](https://programmers.co.kr/learn/courses/30/lessons/42890/)

-----------------------------------

릴레이션의 후보 키를 찾는 문제.

먼저 검사할 모든 칼럼 조합을 combination을 이용해 구하고 나면

이후는 유일성 검정 부분과 최소성 검정 부분으로 나뉘어진다.


    def checkcomb(relation, c, checked_combs, n_row):
        for checked_comb in checked_combs:
                if checked_comb == checked_comb.intersection(set(c)): 
                    return 0
            
        unique = set()
        for row in relation:
            unique.add(''.join([row[i]for i in c]))

        if len(unique)==n_row:
            checked_combs.append(set(c)) 
            return 1
        
        return 0

1. 유일성 

    검사할 칼럼들의 모든 값을 string형태로 이어붙인 후 집합으로 만든다.

    중복값이 있다면 개수가 줄어들었을 것이므로, 개수가 전체 row개수와 같을 경우에만 유일성을 만족한다.

    이후 이 조합을 checked_combs에 추가한다.

2. 최소성

    현재 검사할 칼럼 조합이 이전에 유일성을 만족했던 조합 (checked_combs)들의 전체집합인지 확인한다.
    
    만약 전체집합이라면 이 조합은 최소성을 만족하지 못한다.

다른 코드들도 줄수나 조합을 만드는 방식에 차이는 있지만 전체적인 흐름은 비슷한 것 같다.

최소성 검사하는 부분에서 이중 for 문으로 인해 탈출위치가 잡히지 않았었지만,

해당 부분을 함수화해서 return하는 것으로 해결했다.
    

