n = int(input())
li = list(map(int,input().split()))
stack = []
answer =[-1]*(n)

stack.append(0)
i = 1

while stack and i < n:
    while stack and li[stack[-1]] < li[i]:
        answer[stack[-1]] = li[i]
        stack.pop()
    stack.append(i)
    i += 1
print(*answer)
