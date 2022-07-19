### 시험장 나누기
link : [시험장 나누기 2021 kakao](https://programmers.co.kr/learn/courses/30/lessons/81305)

-----------------------------------

이진트리의 부분집합 중 값이 최대가 되는 값을 찾는 문제.

처음 시도로 k개로 나누어야 하니 k-1개의 간선를 조합해

이를 기준으로 끊었을 때의 최대값을 찾도록 구현해보았다.

정확성 테스트는 모두 통과했지만, 효율성 테스트를 통과하지 못했다.

k와 num의 최대값이 10000이므로 조합이 기하급수적으로 늘어날 수 있기 때문에 어느정도 예상했던 결과이다. 

이 시행착오는 solution_unefficiency.py에 저장되어있다. 

-------------------------------

답을 혼자서 찾아보려고 부단히 노력했지만 마땅한 답을 찾지 못했다.

결국 고생 끝에 Parametric Search 라는 새로운 개념을 배우게 되었다.

Parametric Search는 최적화 문제를 결정 문제로 바꾸어 이진탐색처럼 푸는 방법이다.

이 문제의 경우 '트리를 k개로 나누었을 때의 서브트리의 최댓값 을 최적화' 하는 문제인데,

이를 뒤집어서 '서브트리의 최댓값을 정해두었을 때 이 트리가 나눠지는 개수 를 결정' 하는 문제로 바꾸어 풀 수 있다.

서브트리의 최댓값이 될 수 있는 값은 정해져 있고, 당연히 한 서브트리가 수용할 수 있는 값이

커진다면 트리가 나눠지는 개수는 점차 줄어든다.

따라서 만약 최댓값 후보를 1씩 증가시켜가며 트리가 나눠지는 개수(결과값)를 나열한다면,

서브트리개수 => .....55554444433333.... 이러한 결과값이 나온다.

즉 ***결과값은 차례대로 정렬된 형태고 이 결과값에 이진탐색을 적용***해 역으로 가장 작은 최댓값을 구해낼 수 있다!

그렇다면 일반적인 탐색처럼 모든 값에 트리를 순회할 필요가 없어 효율성이 증가한다.

------------------------------------------------

먼저 트리를 구성하고 루트노드를 구한다.

    tree = dict()
    start = int()

    for i, v  in enumerate(num):
        tree[i] = {'root':-1, 'next' : [], 'value': v}

    for i in tree: 
        for dir in links[i]:
            tree[i]['next'].append(dir)
            if dir != -1:
                tree[dir]['root'] = i

    for i in range(len(num)):
        if tree[i]['root'] == -1:
            start = i
            break

이후 최대값이 될 후보의 범위를 정한다.

범위의 오른쪽 끝은 전체 트리 값의 총합이다.

범위의 왼쪽 끝은 이 총합을 k로 나눈 몫이거나, (나머지가 있을경우 +1)

단일 노드값중 가장 큰 값 중에서 더 큰값이다.

어떤경우에도 이 값들보다 작은 값이 최대치로 제한될 수는 없다.

노드를 가장 균등하게 나눠도 어떤 서브트리의 값의 총합은 전체를 k로 나눈 몫(+1) 이상이고,

단일 노드값보다 작은 값을 최대치로 제한할 수는 없다.

    max_scale = sum(num)
    min_scale = (max_scale//k) +1 if (max_scale % k) > 0 else  max_scale//k 
    min_scale = max(max(num), min_scale)

이 최대값 후보 범위에서 이진탐색을 시작한다.

    while min_scale < max_scale:
        global subcnt
        subcnt = 1
        
        limit_scale = (min_scale + max_scale) //2
        post_sub(tree, start, limit_scale , k)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

시도할 값은 처음과 끝의 중간값이고, 트리가 몇개로 나뉘어지는지 확인하기 위해

post order를 사용한다. 이는 리프노드부터 루트노드까지 차례로 합쳐가며

조건을 만족하는지를 확인하기 위함이다.

후위순열이기 때문에 왼쪽, 오른 쪽 자식 값을 먼저 확인한 후 자신의 값을 반환한다.

이 때 왼쪽/오른쪽 자식 노드의 총합이 자신의 값과 더해졌을 때

적용된 최댓값을 넘는지를 확인하고 각 노드를 자를 지 선택한다.

이렇게 노드가 잘라질 때 마다 그 노드의 총합은 전달되지 않고 서브트리 개수가 증가한다.
    
def post_sub(tree, start, limit_scale, k):
    global subcnt
    # 루트노드일 경우 값을 반환하고 탈출.
    if tree[start]['next'][0] == tree[start]['next'][1] == -1:
        return tree[start]['value']

    # 왼쪽 자식 노드값
    left = 0
    if tree[start]['next'][0] != -1:
        left = post_sub(tree, tree[start]['next'][0], limit_scale, k)
    # 오른 쪽 자식 노드값
    right = 0
    if tree[start]['next'][1] != -1:
        right = post_sub(tree, tree[start]['next'][1], limit_scale, k)

    # 조건문 전개
    root_val = tree[start]['value']
    # 양쪽을 다 더해도 작을 경우
    if root_val + left + right <= limit_scale:
        return root_val + left + right
    # 다 더하면 크지만 둘 중 작은 값을 더해도 작을 경우
    min_leaf = min(left, right)
    if root_val + min_leaf <= limit_scale:
        subcnt += 1
        return root_val + min_leaf 
    # 두 자식 모두 더할 수 없는경우
    subcnt +=2
    return root_val

이렇게 나온 결과값에 따라 이진탐색을 실행한다.

이는 전체 결과값 배열에서에서 k가 들어갈 위치를 찾는것과 같다.

같은 결과값이라도 그 중에서 가장 작은 입력값을 찾아야 하기 때문에

k가 들어갈 위치중 가장 왼쪽을 구해야한다. 즉 bisect_left를 하는것과 같다.

아래 코드는 bisect_left(k)와 동일한 의미이다.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if subcnt > k:
            min_scale = limit_scale + 1
        elif subcnt <= k:
            max_scale = limit_scale

    return min_scale


