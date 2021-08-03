n = int(input())
c0 = [1, 0, 1]
c1 = [0, 1, 1]


def fibo(x):
    if len(c0) <= x:
        for i in range(len(c0), x+1):
            c0.append(c0[i-1]+c0[i-2])
            c1.append(c1[i-1]+c1[i-2])
    print(c0[x], c1[x])


for i in range(n):
    i = int(input())
    fibo(i)
