### 수 정렬하기 3
link : [수 정렬하기 3 sort](https://www.acmicpc.net/problem/10989)

-----------------------------------

카운팅 정렬을 사용하도록 장려하는 문제

카운팅 정렬은 수의 개수는 많더라도 수의 범위가 작더라면

수의 범위를 기준으로 순회를 돌 수 있도록 푸는 문제이다.

각 숫자를 인덱스로 보고 그 인덱스에 숫자의 출현 횟수를 저장하는 count 배열을 만든다.

그리고 count 배열의 누적합 배열을 만들고, 그 누적합 값을 v를 인덱스 숫자i가 들어갈 인덱스로 재치환한다.

예를들어 정렬할 리스트가 [0, 2, 1, 1, 3] 라면, 누적합 배열은 [1, 3, 4, 5] 이다.

즉 인덱스에 해당하는 숫자가 어느 위치에 들어갈지를 정하게 되고, 숫자가 한번 들어가면

누적합 배열에서 -1 해주어 겹치는 숫자가 바로 전 인덱스로 들어가도록 한다.

그러나 이 문제에서는 메모리 제한이 짜기 때문에 각 리스트를 모두 만들수가 없다.

그래서 정렬할 리스트를 굳이 만들지 않고 입력하는 족족 count 함수에 넣어주어 

순서대로 출력만 해주면 된다.