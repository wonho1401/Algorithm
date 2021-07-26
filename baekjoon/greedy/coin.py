N, K = map(int,input().split())
coin = []
cnt = 0
for i in range(N):
    coin.append(int(input()))
    
for i in reversed(coin):
    cnt += K // i
    K%= i
print(cnt)
