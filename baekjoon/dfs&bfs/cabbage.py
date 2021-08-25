import sys
sys.setrecursionlimit(10**6)

case = int(input())

graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)


for _ in range(case):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
