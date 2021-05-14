import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    q = sys.stdin.readline()
    cnt = 0
    flag = 1
    if n == 0:
        li = []
    else:
        li = deque(list(map(int,q.rstrip()[1:-1].split(","))))
    for i in p:
        if i == "R":
            cnt += 1
        elif i == "D":
            if len(li) == 0:
                flag = 0
                break
            if cnt % 2 == 1:
                li.pop()
            elif cnt % 2 == 0:
                li.popleft()
    if cnt % 2 == 1:
        li.reverse()
    if flag == 0:
        print("error")
    else:
        print("[",end="")
        print(*li,sep=",",end="")
        print("]")
            
