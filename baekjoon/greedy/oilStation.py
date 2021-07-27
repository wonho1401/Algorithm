N = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
answer = 0
init = cost[0]

for i in range(N-1):
    if cost[i] < init:
        init = cost[i]
    answer += init*dist[i]
print(answer)
