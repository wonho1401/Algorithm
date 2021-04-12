def solution(brown, yellow):
    all = brown + yellow 
    x = (brown + 4 + ((brown + 4)** 2 - 16*all)**0.5) / 4
    y = all / x
    answer = [x,y]
    return answer
