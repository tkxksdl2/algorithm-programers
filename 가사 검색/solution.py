import bisect

def solution(words, queries):
    answer = []
    words_reverse = [i[::-1] for i in words]

    words.sort()
    words.sort(key=lambda i:len(i))

    words_reverse.sort()
    words_reverse.sort(key=lambda i:len(i))

    print(words)
    print(words_reverse)

    # 글자수순으로 정렬하고 경계 인덱스 저장
    
    wordslen_idxs = get_wordslen_idx(words)


    query_lib = dict()
    for query in queries:
        if query in query_lib.keys():
            answer.append(query_lib[query])
            continue


        head = query.startswith('?')
        tail = query.endswith('?')
        length = len(query)
        cnt = 0

        if length not in wordslen_idxs.keys():
            answer.append(cnt)
            query_lib[query] = cnt
            continue
            
            
        
        if head and tail:
            length_match_list = words[wordslen_idxs[length][0]: wordslen_idxs[length][1]]
            cnt = len(length_match_list)

        elif head:
            query_reverse = query[::-1]
            cnt = bisect_getcount(words_reverse,wordslen_idxs, length, query_reverse)

        else:
            cnt = bisect_getcount(words, wordslen_idxs,length, query)

        query_lib[query] = cnt
        answer.append(cnt)


    return answer

words = ["frodo", 'muyah',"front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def get_wordslen_idx(words):
    w_len = 0
    lenthup_idxs = {0:[0]}
    
    for w in words:
        if len(w) > w_len:
            lenthup_idxs[len(w)] = [words.index(w)]
            lenthup_idxs[w_len] += [words.index(w)]
            w_len = len(w)
    lenthup_idxs[w_len] += [len(words)]
    print(lenthup_idxs)

    return lenthup_idxs

def bisect_getcount(words,wordslen_idxs, length, query):
    length_match_list = words[wordslen_idxs[length][0]: wordslen_idxs[length][1]]
    start_key = query.replace('?','a')
    end_key = query.replace('?','z')

    start = bisect.bisect_left(length_match_list, start_key)
    end = bisect.bisect_right(length_match_list, end_key)

    cnt = end - start
    return cnt


print(solution(words,queries))