n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li = sorted(li)
for i in li:
    print(i,end="\n")
