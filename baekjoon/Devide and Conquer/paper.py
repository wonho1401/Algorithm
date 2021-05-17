import sys
N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
w, b = 0, 0
def check(i, j, k):
    color = li[i][j]
    for x in range(i, i+k):
        for y in range(j, j+k):
            if li[x][y] != color:
                return False
    return True

def recursion(i, j, k):
    global w, b
    if check(i, j, k) == True:
        if li[i][j] == 1:
            b += 1
        else:
            w += 1
        return
    else:
        k //= 2
        recursion(i, j, k)
        recursion(i+k, j, k)
        recursion(i, j+k, k)
        recursion(i+k, j+k, k)
        return 
recursion(0,0,N)
print(w)
print(b)
