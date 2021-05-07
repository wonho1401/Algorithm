import sys
n = int(sys.stdin.readline())

queue = []
index = 0
cnt = 0
for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == "push":
        queue.append(int(x[1]))
        cnt += 1
    elif x[0] == "front":
        if cnt == 0:
            print("-1")
        elif index < len(queue):
            print(queue[index])
    elif x[0] == "back":
        if cnt == 0:
            print("-1")
        elif index < len(queue):
            print(queue[-1])
    elif x[0] == "size":
        print(cnt)
    elif x[0] == "empty":
        if cnt == 0:
            print("1")
        else:
            print("0")
    elif x[0] == "pop":
        if cnt == 0:
            print("-1")
        elif index < len(queue):
            print(queue[index])
            index += 1
            cnt -= 1
        
