## 캐시
Link : [캐시 kaka0 2018](https://programmers.co.kr/learn/courses/30/lessons/17680/)

--------------------------------------------

알고리즘보다는 캐시에 대한 이해도를 요구하는 문제

효율성검정도 없어서 쉽게 풀었다.

LRU은 교체대상이 될 원소를 항상 0번째 인덱스에 배치하도록 구현했다.

다른 사람 코드 중에 참고할만한 부분은

    collections.deque(maxlen=cacheSize)

이렇게 maxsize를 설정한 큐를 이용해 코드수를 줄일 수도 있었다.