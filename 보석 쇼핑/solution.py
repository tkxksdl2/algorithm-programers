def solution(gems):
    unique_len = len(set(gems))
    start, end = 0, 0
    selected_dict = dict()
    answer = [len(gems), 0, len(gems)]

    while True:
        if len(selected_dict.keys()) == unique_len:
            if (end - start ) < answer[0]:
                answer = [end - start, start, end]
            
            if selected_dict[gems[start]] > 1:
                selected_dict[gems[start]] -= 1
            else:
                selected_dict.pop(gems[start])
            start+=1

        else:
            if end == len(gems):
                return [answer[1]+1, answer[2]]
            
            if gems[end] in selected_dict:
                selected_dict[gems[end]] += 1
            else: selected_dict[gems[end]] = 1
            end += 1


    



gems = ["DIA", "EM", "EM", "RUB", "DIA"]

print(solution(gems))