def solution(d, budget):
    d.sort()
    _sum = 0
    answer = 0
    for i in d:
        _sum += i
        if _sum > budget:
            break
        else:
            answer +=1
    return answer
