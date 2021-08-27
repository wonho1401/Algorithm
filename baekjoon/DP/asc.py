n = int(input())
dp = [[0]*10 for _ in range(n)]
answer = 0
if n == 1:
    print(10)
else:
    dp[1] = [1,2,3,4,5,6,7,8,9,10]
    for i in range(2, n):
        for j in range(10):
            dp[i][j] = ( dp[i-1][j] + dp[i][j-1] ) % 10007
    print(sum(dp[n-1]) % 10007)
