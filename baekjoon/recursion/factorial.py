n = int(input())

def fact(k):
    if k == 0:
        return 1
    else:
        return fact(k-1)*k
print(fact(n))
