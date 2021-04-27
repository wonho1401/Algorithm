n = int(input())
li = list(map(int,input().split()))
sorted_li = sorted(list(set(li)))
dic ={value: i for i , value in enumerate(sorted_li)}
for i in li:
    print(dic[i],end=" ")
