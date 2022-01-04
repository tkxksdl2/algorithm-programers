import bisect

def solution(words, queries):
    answer = []
    words_reverse = [i[::-1] for i in words]

    words.sort()
    words.sort(key=lambda i:len(i))
    
    
    words_reverse.sort()
    words_reverse.sort(key=lambda i:len(i))

    # 글자수순으로 정렬하고 경계 인덱스 저장
    wordslen_idxs = get_wordslen_idx(words)

    # 한 번 검색한 쿼리를 기억함
    query_lib = dict()
    
    for query in queries:
        if query in query_lib.keys():
            answer.append(query_lib[query])
            continue

        # 쿼리의 종류 확인
        head = query.startswith('?')
        tail = query.endswith('?')
        
        length = len(query)
        cnt = 0
        
        # 맞는 길이가 없다면 자동으로 0 반환
        if length not in wordslen_idxs.keys():
            answer.append(cnt)
            query_lib[query] = cnt
            continue
                
        # 모두 ? 인 경우 글자수가 맞는 경우 모두 반환
        if head and tail:
            length_match_list = words[wordslen_idxs[length][0]: wordslen_idxs[length][1]]
            cnt = len(length_match_list)

        # 앞이 ? 이면 뒤집힌 words에서 검색
        elif head:
            query_reverse = query[::-1]
            cnt = bisect_getcount(words_reverse,wordslen_idxs, length, query_reverse)
            
        # 뒤가 ? 인 경우 기본 words 에서 검색
        else:
            cnt = bisect_getcount(words, wordslen_idxs,length, query)

        query_lib[query] = cnt
        answer.append(cnt)


    return answer

# 글자수에 따라 정렬된 리스트에서 글자수 변하는 위치 저장
def get_wordslen_idx(words):
    w_len = 0
    lenthup_idxs = {0:[0]}
    
    for w in words:
        if len(w) > w_len:
            lenthup_idxs[len(w)] = [words.index(w)]
            lenthup_idxs[w_len] += [words.index(w)]
            w_len = len(w)
    lenthup_idxs[w_len] += [len(words)]

    return lenthup_idxs

# bisect를 이용해 쿼리의 시작점과 끝점으로 개수 파악
def bisect_getcount(words,wordslen_idxs, length, query):
    length_match_list = words[wordslen_idxs[length][0]: wordslen_idxs[length][1]]
    start_key = query.replace('?','a')
    end_key = query.replace('?','z')

    start = bisect.bisect_left(length_match_list, start_key)
    end = bisect.bisect_right(length_match_list, end_key)

    cnt = end - start
    return cnt