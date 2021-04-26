import sys
n = int(input())
x = []
for _ in range(n):
    a, b = map(int , sys.stdin.readline().split() )
    x.append((a,b))
x = sorted(x,key = lambda x: (x[1],x[0]))
for i in range(len(x)):
    print(x[i][0],x[i][1])
