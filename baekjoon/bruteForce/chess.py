n, m = map(int,input().split())
chess = []
ans = []
for _ in range(n):
    chess.append(input())
for i in range(n-7):
    for j in range(m-7):
        flag1 = 0
        flag2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != "W":
                        flag1 += 1
                    if chess[a][b] != "B": 
                        flag2 += 1
                else:
                    if chess[a][b] != "B": 
                        flag1 += 1
                    if chess[a][b] != "W": 
                        flag2 += 1
        ans.append(flag1)
        ans.append(flag2)
print(min(ans))
