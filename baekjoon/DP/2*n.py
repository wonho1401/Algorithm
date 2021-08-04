n = int(input())

li = [0]* n

li[0] = 1

if n == 1:
    print(1)
    exit()

li[1] = 2

for i in range(2,n):
    li[i] = li[i-1]+li[i-2]
print(li[n-1] % 10007)
