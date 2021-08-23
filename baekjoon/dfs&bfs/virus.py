n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
answer = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(s, visited=[False]*(n+1)):
    visited[s] = True
    answer.append(s)
    for i in range(len(graph[s])):
        if graph[s][i] == 1 and not visited[i]:
            dfs(i, visited)

            
dfs(1)
print(len(answer)-1 )
