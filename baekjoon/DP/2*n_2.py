n = int(input())

li = [1,3,5]

if n == 1:
    print(li[0])
    exit()
elif n == 2:
    print(li[1])
    exit()
for i in range(3,n):
    if i % 2 == 0:
        li.append(li[i-1]*2 - 1)
    else:
        li.append(li[i-1]*2 + 1)
print(li[-1]%10007)
