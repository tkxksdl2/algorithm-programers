import re

def solution(word, pages):
    page_dict = dict()
    urlfinder = re.compile('https://(.+)"')
    
    for idx, page in enumerate(pages):
        page = page.lower()
        # 메타 태그와 주소 추출
        meta = re.search('<meta(.+)/>', page).group()
        self_url = urlfinder.search(meta).group()
        # body 태그 추출
        body = re.search('<body.+body>',page, re.S).group()
        # a태그 추출
        links = re.findall('<a(.+?)>',body)
        if links:
            for i, link in enumerate(links):
                links[i] = urlfinder.search(link).group()
        else:   # 링크가 없는 경우 예외처리
            links = []
        # 전체 페이지에서 영문 알파벳을 제외한 나머지를 .으로 변경 후 나눔
        # 이 알파벳 리스트에서 word를 검색한다.
        # 태그에 word와 겹치는 알파벳이 없기 때문에 가능.
        wordcnt = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
        # index와 외부링크, 기본점수, 매칭점수를 가진 딕셔너리
        page_dict[self_url] = {'index':idx, "to":links, "basic":wordcnt, "mat":wordcnt}

    answer = None
    max_score = -1
    # 각 매칭점수 설정
    for page in page_dict.values():
        if page['to']:
            link_point = page['basic'] / len(page['to'])
            for link in page['to']:
                if link in page_dict:
                    page_dict[link]['mat'] += link_point
    # 각 매칭점수 비교
    for page in page_dict.values():
        if page['mat'] > max_score:
            answer = page['index']
            max_score = page['mat']

    return answer

word = "blind"
pages =["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.c./com\"/>\n</head>  \n<body>\nBlind Lorem Blind  blind@blind@blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]


print(solution(word, pages))