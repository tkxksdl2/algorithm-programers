## 효율성 통과 못함.

def solution(words, queries):
    answer = []

    for query in queries:
        head = query.startswith('?')
        tail = query.endswith('?')
        length = len(query)

        cnt = 0
        idx_list = []
        for w in words:
            if len(w) == length:
                idx_list.append(words.index(w))

        #print(idx_list)

        if head and tail:
            cnt = len(idx_list)
        elif head:
            key = query.split('?')[-1]
            for idx in idx_list:
                if words[idx].endswith(key):
                    cnt += 1
        else:
            key = query.split('?')[0]
            for idx in idx_list:
                if words[idx].startswith(key):
                    cnt += 1

        answer.append(cnt)


    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))