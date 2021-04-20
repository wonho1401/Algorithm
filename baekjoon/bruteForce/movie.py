N = int(input())
m = 666
c = 0
while(True):
    if "666" in str(m):
        c += 1
        if c == N:
            print(m)
            break
    m += 1
