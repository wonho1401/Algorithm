import sys
n = int(input())
li = []
count = [0]*8001
common = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
print(round(sum(li)/len(li)))
li = sorted(li)
print(li[int(len(li)/2)])
for i in range(len(li)):
    count[li[i]+4000] += 1
for i in range(len(count)):
    if count[i] == 0: continue
    if count[i] == max(count):
        common.append(i-4000)
if len(common) == 1:
    print(common[0])
else:
    print(common[1])
print(li[len(li)-1]-li[0])
