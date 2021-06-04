def solution(citations):
    answer = 0
    citations = sorted(citations,reverse=True)
    h = len(citations)
    while True:
        c = 0
        for cit in citations:
            if cit >= h:
                c += 1
            if c >= h:
                return h
        h -= 1
