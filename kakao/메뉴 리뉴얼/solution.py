
def solution(orders, course):
    order_cnt_dict =dict()
    for n in course:
        order_cnt_dict[n] = dict()

    for order in orders:
        for n in course:
            if n <= len(order):
                result = combination(order, n)

                for menu in result:
                    menu.sort()

                    setmenu = ''.join(menu)

                    if setmenu not in order_cnt_dict[n].keys():
                        order_cnt_dict[n][setmenu] = 1
                    else:
                        order_cnt_dict[n][setmenu] += 1

    result = []
    for n in course:
        if not order_cnt_dict[n]:
            continue
        max_cnt = max(order_cnt_dict[n].values())

        if max_cnt >=2:
            for setmenu, cnt in order_cnt_dict[n].items():
                if cnt == max_cnt: result.append(setmenu)
    result.sort()

    return result



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



orders = 	["XYZ", "XWY", "WXA"]
course = [2,3,4]
result = solution(orders, course)
print('result : ', result)