## 오픈채팅방
Link : [추석 트래픽](https://programmers.co.kr/learn/courses/30/lessons/17676/)

--------------------------------------------

리스트 정렬 후 이진탐색을 이용한 검색을 활용했다.

리스트가 적어서 굳이 이진탐색을 쓸 필요는 없었던 것 같지만,

흐름은 다음과 같다.

1. 시간을 int형으로 변경

2. 각 log를 시작시간과 끝시간으로 나누어 정렬

3. 특정 log의 끝부분마다 1초 구간을 잡고 검사.

4. 1초구간 경계선을 bisect를 이용해, 좌 우 index를 찾고,

    이 좌우 index를 이용해 구간에 들어가는 log 개수를 찾음

5. 반복 후 최대값 반환


처음에 완전탐색이라고 생각해 모든 시간초 단위를 검사했었는데,

왜 그렇게 생각했었는지 모르겠다. 당연히 timeout이 걸렸었다.

최대 개수를 찾으려면 당연히 어떤 log의 가장 끝부분을 검사하는것이 효율적이다.

다음에는 bisect를 직접 구현해서 만들어보고싶다.