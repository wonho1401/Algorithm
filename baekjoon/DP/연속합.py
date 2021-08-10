n = int(input())
li = list(map(int, input().split()))
answer = [0] * n
answer[0] = li[0]
for i in range(1, n):
    answer[i] = max(li[i], li[i]+answer[i-1])
print(max(answer))
