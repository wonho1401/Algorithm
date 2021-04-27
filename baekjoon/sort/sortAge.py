n = int(input())
li =[]
num = 0
for _ in range(n):
    age, name = input().split()
    num += 1
    li.append((int(age),name, num))
li = sorted(li,key = lambda x: (x[0], x[2]))

for i in range(len(li)):
    print(li[i][0],li[i][1])
