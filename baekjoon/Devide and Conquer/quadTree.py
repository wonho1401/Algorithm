import sys
N = int(sys.stdin.readline())
li = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = []
def recursion(i, j, k):
    global answer
    color = li[i][j]
    for x in range(i,i+k):
        for y in range(j,j+k):
            if color != li[x][y]:
                k //= 2
                answer.append("(")
                recursion(i, j, k)
                recursion(i ,j+k ,k)
                recursion(i+k, j ,k)
                recursion(i+k, j+k, k)
                answer.append(")")
                return
    answer.append(color)
recursion(0,0,N)
print("".join(answer))
