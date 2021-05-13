import sys
n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == "push_front":
        deque.insert(0,x[1])
    elif x[0] == "push_back":
        deque.append(x[1])
    elif x[0] == "pop_front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop(0))
    elif x[0] == "pop_back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque.pop())
    elif x[0] == "size":
        print(len(deque))
    elif x[0] == "empty":
        if len(deque) == 0:
            print("1")
        else:
            print("0")
    elif x[0] == "front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])
    elif x[0] == "back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[-1])
