### 길 찾기 게임
link : [길 찾기 게임 kakao 2019](https://programmers.co.kr/learn/courses/30/lessons/42892/)

-----------------------------------

트리와 순회를 적절히 혼합한 문제.

문제 로직자체는 크게 어렵지 않지만, 코딩에 시간이 좀 걸리고

문제 설명이 약간 애매해서 조금 헤멨다.

처음엔 별다른 부모와 자식이 어떻게 연결되는지에 관해 별 조건이 없다고 생각해서

좌표의 맨해튼 거리가 가장 짧은 부모자식이 연결되도록 설정했었다.

하지만 역시 정답이 아니었고 다시 살펴보니 조건을 알 수 있었다.

어떤 노드의 좌측, 우측에 있는 서브노드의 x값은 무조건 그 노드의 x값보다 좌측, 우측에 있다.

이것을 그림으로 나타내면 다음과 같다.

<img src="./img/001.jpg" width="400" height="200"/>

이렇게 자식노드의 연결관계는 부모 노드의 경계선에의해 제한된다.

그렇기 때문에 직전 레벨의 노드들의 바운더리를 조사하면

현재 자식노드가 어떤 노드와 관계가 형성되어야 할지 알 수 있다.

때문에 트리의 구성은 루트노드부터 레벨별로 진행되어야 했고,

이를 위해서 전체 nodeinfo를 y값의 내림차순으로 정렬해야했다.

트리가 올바르게 만들어지고 나면 남은 것은 전열순회와 후열순회를 한 결과값을 만들기만 하면 끝난다.

이것은 간단하게 재귀를 이용해 구현했다.

    def order(tree, start, res, pre=True):
        if pre: res.append(start)
        q = deque(tree[start]['child'])
        while q:
            if pre: order(tree, q.popleft(), res)
            else:   order(tree, q.popleft(), res, pre=False)
        if not pre: res.append(start)
        return