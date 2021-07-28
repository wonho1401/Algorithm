n = int(input())
li = sorted([list(map(int,input().split()))for _ in range(n)],key = lambda x: (x[1],x[0]))
answer = 0
temp = 0
for s,e in li:
    if s >= temp:
        answer += 1
        temp = e
print(answer)
