### 표 편집
link : [표 편집 카카오 2021 ](https://programmers.co.kr/learn/courses/30/lessons/81303/)

-----------------------------------

표에서 포인터의 위치를 지정하고 삭제, 되돌리기 하는것을 구현하는 문제.

문제를 푸는 데 중요한 제한사항이 몇 가지 있다.

1. 지우는 것은 포인터 위치로. 지운 이후 포인터는 아래 값을 가리킨다.

    지운값이 끝 값일 경우 윗값을 가리킨다.

2. 되돌리는 것은 지웠을 당시의 위치로. 포인터 값에는 영향을 끼치지 않는다.

처음엔 효율성 문제를 생각하지 않고 리스트를 이용해 간단하게 구현해 보았다.

정확도는 통과했지만, 문제가 되는 부분은 list.insort() 부분으로,

insort() 자체가 O(N)의 복잡도를 가지기 때문에 되돌리기 할 때마다 너무 많은 연산을 했다.

하나의 값을 중간에 넣기 위해 나머지 값을 모두 재설정하기 때문이다.

이 시행착오는 solution_unefficient.py에 기록되어 있다.

------------------------------------

이를 해결하기 위해서 자료구조를 Doubly linked list로 바꾸어서 다시 구현했다.

각 리스트가 앞 - 뒤로 연결되는 값의 주소를 가지고 있기 때문에,

실제로 값을 지우거나 다시 넣지 않고 앞-뒤값의 주소를 바꿔주는 것 만으로도

값의 삭제와 복원을 구현할 수 있다.

이 방법이 가능한 이유는

1. 첫 포인터 이후로 포인터는 ***주소를 기준으로 참조되지 않는다.*** 오직 이전 값, 이후 값으로 이동하기만 한다.

2. 되돌리기는 모두 삭제되었던 순서의 ***역순으로만 진행된다***. 즉, 지금 복원할 값과 연결되야 할 

    앞 뒤 값은 항상 연결에 존재한다.

값을 삭제할 때는 값의 이전값과 이후값을 연결해주고,

값을 다시 복원할 때는 복원할 값이 삭제되었을 당시의 이전값과 이후값을

복원할 값과 연결해주기만 하면 된다.

    class LinkedList():
    ~~~~~~~~~~~~~~~~~~~~~~~~
        def clear(self):
            self.deleted.append(self.pointed)
            if self.pointed['pre'] != None:
                self.lst[self.pointed['pre']]['next'] = self.pointed['next']
            if self.pointed['next'] != None:
                self.lst[self.pointed['next']]['pre'] = self.pointed['pre']
                self.next_point(1)
                return
            self.pre_point(1)

        def undo(self):
            undo_point = self.deleted.pop()
            if undo_point['pre'] != None:
                self.lst[undo_point['pre']]['next'] = undo_point['value']
            if undo_point['next'] != None:
                self.lst[undo_point['next']]['pre'] = undo_point['value']

Linked list를 스스로 구현해 본 것은 처음이라 즐겁게 진행했다.

