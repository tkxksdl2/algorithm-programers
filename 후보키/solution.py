from itertools import combinations
def solution(relation):
    n_col = len(relation[0]) 
    n_row = len(relation)
    answer = 0

    combs=[]
    for i in range(1, n_col+1):
        combs.extend(combinations(range(n_col), i))
        
    checked_combs = []

    for c in combs:
        answer += checkcomb(relation, c, checked_combs, n_row)
            
    return answer

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
         

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(solution(relation))
