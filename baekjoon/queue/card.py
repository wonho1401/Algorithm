from collections import deque

n = int(input())

queue = deque([i+1 for i in range(n)])

while len(queue) > 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
print(queue[0])
