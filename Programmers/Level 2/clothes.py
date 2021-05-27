from collections import Counter

def solution(clothes):
    dic = Counter([c for _, c in clothes])
    answer = 1
    for key in dic:
        answer *= dic[key] + 1
    return answer-1
