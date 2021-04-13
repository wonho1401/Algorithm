from itertools import combinations

n, m = input().split()
nums = [int(x) for x in input().split()]
li = []
sum_li = []
for i in combinations(nums,3):
    li.append(list(i))
for i in range(len(li)):
    if(int(sum(li[i]))) <= int(m):
        sum_li.append(sum(li[i]))
print(max(sum_li))
