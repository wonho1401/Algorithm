def solution(n):
    x = [0]*(n+1)
    x[0] = 0
    x[1] = 1
    for i in range(2,n + 1):
        x[i] = x[i-1]+x[i-2]
    return x[n] % 1234567
