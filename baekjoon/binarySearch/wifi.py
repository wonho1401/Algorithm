N , C = map(int,input().split())
li = []
for _ in range(N):
    li.append(int(input()))
li.sort()

start = 1
end = li[-1] - li[0]
answer = []

while start <= end:
    temp = li[0]
    mid = (start + end) // 2
    cnt = 1
    for i in range(1, len(li)):
        if temp + mid <= li[i]:
            temp = li[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        answer.append(mid)
    else:
        end = mid - 1
print(max(answer))
