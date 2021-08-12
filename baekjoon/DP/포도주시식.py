n = int(input())
li = []
dp = [0]*n
for i in range(n):
    li.append(int(input()))
if n == 1:
    print(li[0])
elif n == 2:
    print(li[0]+li[1])
elif n == 3:
    print(max(li[2]+li[0], li[1]+li[2], li[0]+li[1]))
else:
    dp[0] = li[0]
    dp[1] = li[0]+li[1]
    dp[2] = max(li[2]+li[0], li[1]+li[2], li[0]+li[1])
    dp[3] = max(dp[0]+li[2]+li[3], dp[1]+li[3])
    for i in range(4, n):
        dp[i] = max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i], dp[i-4]+li[i-1]+li[i])
    print(max(dp))
