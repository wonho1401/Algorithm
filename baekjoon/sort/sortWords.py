n = int(input())
li =[]
for _ in range(n):
    w = str(input())
    w_li = len(w)
    li.append((w_li,w))
li = list(set(li))
li = sorted(li,key=lambda x: (x[0],x[1]))
for i in range(len(li)):
    print(li[i][1])
