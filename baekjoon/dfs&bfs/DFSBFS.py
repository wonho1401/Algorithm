from collections import deque

n , m , v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(s, visited = [False]*(n+1)):
    visited[s] = True
    print(s, end=" ")
    for i in range(len(graph[s])):
        if graph[s][i] == 1 and not visited[i]:
            dfs(i,visited)
            
            
def bfs(s, visited= [False]*(n+1)):
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end= " ")
        for i in range(len(graph[s])):
            if graph[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                

dfs(v)
print()
bfs(v)
