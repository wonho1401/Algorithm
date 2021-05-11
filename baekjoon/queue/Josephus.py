from collections import deque

n , k = map(int,input().split())

queue = deque([i+1 for i in range(n)])
li = []
num = 0
while len(queue) > 0 :
    num += k - 1
    if num >= len(queue):
        num = num % len(queue)
    li.append(queue[num])
    del queue[num]
print("<",end="")
print(*li,sep=", ",end="")
print(">")
