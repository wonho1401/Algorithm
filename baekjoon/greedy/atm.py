n = int(input())
li = sorted(list(map(int,input().split())))

for i in range(1,len(li)):
    li[i] += li[i-1]
print(sum(li))
