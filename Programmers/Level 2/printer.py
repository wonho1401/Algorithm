from collections import deque
def solution(priorities, location):
    answer = 0
    li = deque([])
    cnt = 0
    for i in range(len(priorities)):
        li.append([priorities[i],i])
    while li:
        top = max(li)
        pop = li.popleft()
        if top[0] != pop[0]:
            li.append(pop)
        else:
            cnt += 1
            if location == pop[1]:
                answer = cnt
                break
    return answer
