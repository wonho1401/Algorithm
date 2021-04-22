import sys
n = int(input())
li = [0]*10001
for i in range(n):
    num = int(sys.stdin.readline())
    li[num] += 1
for i in range(len(li)):
    if li[i] !=0:
        for _ in range(li[i]):
            print(i)
