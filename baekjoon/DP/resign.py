n = int(input())
li = []
dp = [0]*(n+1)
for i in range(n):
    t, p = map(int, input().split())
    li.append([t, p])
for i in range(n-1, -1, -1):
    if i + li[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+li[i][0]]+li[i][1])
print(max(dp))
