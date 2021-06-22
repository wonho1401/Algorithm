from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        count = 0
        v = queue.popleft()
        for q in queue:
            count += 1
            if v > q:
                break
        answer.append(count)
    return answer
