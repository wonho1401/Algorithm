import math 
import collections
def solution(progresses, speeds):
    answer = []
    flag = 0
    count = 0
    h = [100]*len(progresses)
    for i in range(len(h)):
        progresses[i] = h[i] - progresses[i]
        progresses[i] = math.ceil(progresses[i] / speeds[i])
    flag=progresses[0]
    for i in range(len(progresses)):
        if flag < progresses[i]:
            flag = progresses[i]
        answer.append(flag)
    answer = collections.Counter(answer)

    return list(answer.values())
