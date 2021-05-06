n = int(input())
stack = []
result = []
cnt = 0
flag = 1
for _ in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = 0
        break
if flag == 0:
    print("NO")
else:
    for i in result:
        print(i)
        
