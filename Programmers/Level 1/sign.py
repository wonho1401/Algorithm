def solution(absolutes, signs):
    li =list(zip(absolutes,signs))
    answer = 0
    for n,s  in li:
        if s:
            answer += n
        else:
            answer -= n
    return answer
