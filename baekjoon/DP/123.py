n = int(input())
li = [0,1,2,4]

for i in range(4,12):
    li.append(li[i-3] + li[i-2] + li[i-1])

for i in range(n):
    k = int(input())
    print(li[k])
