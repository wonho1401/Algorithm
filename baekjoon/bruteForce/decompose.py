num = int(input())
answer = 0
for i in range(1,num + 1):
    n_map = list(map(int,str(i)))
    answer = i + sum(n_map)
    if num == answer:
        print(i)
        break
    if num == i:
        print(0)
