n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
if n == 1:
    dp = [li[0]]
elif n == 2:
    dp = [li[0],li[0]+li[1]]
else:
    dp = [li[0],li[0]+li[1],max(li[0]+li[2],li[1]+li[2])]
    for i in range(3, n):
        dp.append(max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i]))
print(dp[-1])
