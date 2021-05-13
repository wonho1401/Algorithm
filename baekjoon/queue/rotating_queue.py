import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
dq = deque([i+1 for i in range(N)])
arg = [int(i) for i in sys.stdin.readline().split()]
cnt = 0
while len(arg) > 0:
    if dq.index(arg[0]) < len(dq) - dq.index(arg[0]):
        for _ in range(dq.index(arg[0])):
            x = dq.popleft()
            dq.append(x)
            cnt += 1
        dq.popleft()
        arg.pop(0)
        if len(arg) == 0:
            print(cnt)
            break
    else:
        for _ in range(len(dq) - dq.index(arg[0])):
            x = dq.pop()
            dq.appendleft(x)
            cnt += 1
        dq.popleft()
        arg.pop(0)
        if len(arg) == 0:
            print(cnt)
            break
