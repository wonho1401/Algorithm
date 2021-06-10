from collections import deque

def solution(N, stages):
    stages.sort()
    stage = 1
    length = len(stages)
    answer = []
    fail = []
    while stage <= N:
        cnt = 0
        for i in stages:
            if i == stage:
                cnt += 1
            if i > stage:
                break
        if length == 0:
            fail.append((0,stage))
        else:
            fail.append(((cnt / length),stage))
        length -= cnt
        stage += 1
    fail = sorted(fail,key = lambda x:-x[0])
    for a,b in fail:
        answer.append(b)
    return answer
