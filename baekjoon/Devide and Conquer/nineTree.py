import sys
N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a,b,c = 0, 0, 0
def check(i, j, k):
    color = li[i][j]
    for x in range(i, i+k):
        for y in range(j, j+k):
            if li[x][y] != color:
                return False
    return True

def recursion(i, j, k):
    global a, b, c
    if check(i, j, k) == True:
        if li[i][j] == 1:
            c += 1
        elif li[i][j] == 0:
            b += 1
        else:
            a += 1
        return
    else:
        k //= 3
        recursion(i, j, k)
        recursion(i, j+k, k)
        recursion(i, j+k+k, k)
        recursion(i+k, j, k)
        recursion(i+k, j+k, k)
        recursion(i+k, j+k+k, k)
        recursion(i+k+k, j, k)
        recursion(i+k+k, j+k, k)
        recursion(i+k+k, j+k+k, k)
        return
recursion(0,0,N)
print(a)
print(b)
print(c)
