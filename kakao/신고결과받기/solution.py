def solution(id_list, report, k):
    report_dict = {id:[] for id in id_list}
    answer = [0 for _ in range(len(id_list))]
    
    for r in report:
        a, b = r.split()
        report_dict[b].append(a)
    
    for id in id_list:
        report_list =set(report_dict[id])
        
        if len(report_list) >= k:
            for id in report_list:
                answer[id_list.index(id)] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


print(solution(id_list, report, k))