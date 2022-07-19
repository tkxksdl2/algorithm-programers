def solution(numbers, hand):
    l_fix = [1,4,7]
    r_fix = [3,6,9]

    answer = ''
    numbers = [n if n != 0 else 11 for n in numbers ]

    l_fin = 10 # 손가락 위치
    r_fin = 12

    for n in numbers:
        if n in l_fix:
            answer += "L"; l_fin = n
            continue
        elif n in r_fix:
            answer += "R"; r_fin = n
            continue
        
        dists = []
        for fin in [l_fin, r_fin]:
            m, l  = divmod(abs(n-fin), 3) 
            dists.append(m + l)
        
        if dists[0] == dists[1]:
            if hand == 'left':
                answer +='L'; l_fin = n
            else:
                answer += "R"; r_fin = n

        elif dists[0] < dists[1]:
            answer +='L'; l_fin = n

        else:
            answer += "R"; r_fin = n

    
    return answer


numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
# result = 	"LRLLRRLLLRR"

s = solution(numbers, hand)
print(s)