n = int(input())

k = n // 5
cnt = 0
while True:
    if k == -1:
        print(-1)
        break
    r = n - 5*k
    if r % 3 == 0:
        cnt = k + r // 3
        print(cnt)
        break
    k -= 1
