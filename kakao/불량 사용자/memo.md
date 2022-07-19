### 불량 사용자
link : [불량 사용자 카카오 2019](https://programmers.co.kr/learn/courses/30/lessons/64064/)

-----------------------------------
이번엔 DFS를 사용한 문제로 처음 구상에 많은 어려움을 겪었다.

처음엔 가사검색과 같이 구간을 * 위치에 따라 구간을 검색하려 했지만,

*가 중간에 있는 경우를 처리하지 못해 곤란을 겪었다.

나중에서야 입력 리스트의 길이가 8 이하로 매우 짧다는 것을 알고

단순 검색으로 처리하도록 했다.

코드의 흐름은 다음과 같다.

1. 주어진 banned_id 의 개체 당 가능한 사용자 아이디 리스트를 검색해 저장한다.

2. 저장한 리스트들을 DFS을 사용해 가능한 순열을 구한다.

3. 중복을 제거하고, 개수를 반환한다.

2번 과정에서 여러 리스트에서 순열을 구하는 코드가 필요했다.

이는 itertools의 product를 사용하면 쉽게 구현할 수 있었지만,

최악의 경우 (모든 ban이 *8 이고, 모든 user 가 8글자인 경우) 8^8의 계산으로 오류가 난다는 점이 문제였다.

때문에 python 공식 홈페이지에서 pruduct함수를 참고하여 약간의 수정을 거쳤다.

[product 설명](https://docs.python.org/3.8/library/itertools.html#itertools.product)

    for possible_set in possible_set_lst:
            res = [x + [y] for x in res for y in possible_set if y not in x ]

컴프리헨션 내 조건을 사용해 중복이 있는 경우를 검열했고, 

때문에 순열에 중복이 있는 경우 바로 제거하여 최악의 경우의 

경우의 수가 8^8 = 16777216 에서 40320으로 엄청나게 줄일 수 있었다.
