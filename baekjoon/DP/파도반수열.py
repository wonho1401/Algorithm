n = int(input())

for i in range(n):
    li = [1, 1, 1, 2, 2]
    k = int(input())
    for x in range(5, k+1):
        li.append(li[x-1]+li[x-5])
    print(li[k-1])
