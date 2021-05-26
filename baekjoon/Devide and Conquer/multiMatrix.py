import sys
n,m = map(int,sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m,k = map(int,sys.stdin.readline().split())
b = list(zip(*[list(map(int, sys.stdin.readline().split())) for _ in range(m)]))
answer = [[sum(map(lambda x:x[0]*x[1],zip(a[i],b[j]))) for j in range(k)] for i in range(n)]

for i in answer:
    print(*i)
