from collections import deque
import sys

x = int(sys.stdin.readline())
for _ in range(x):
    n, m = map(int, sys.stdin.readline().split())
    q = deque(map(int, sys.stdin.readline().split()))
    q_tuple = []
    cnt = 0
    for i in range(len(q)):
        q_tuple.append([q[i], i])
    # top = max(q_tuple)
    # print(top[0])
    while q_tuple:
        top = max(q_tuple)
        pop = q_tuple.pop(0)
        if top[0]!= pop[0]:
            q_tuple.append(pop)
        else:
            cnt += 1
            if m == pop[1]:
                print(cnt)
                break
