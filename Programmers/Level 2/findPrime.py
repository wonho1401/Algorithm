from itertools import permutations
import math

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    _li = []
    primeLi = []
    for i in numbers:
        _li.append(i)
    for i in range(1,len(_li)+1):
        for j in permutations(_li,i):
            primeLi.append("".join(j))
    primeLi = set(list(map(int,primeLi)))
    for i in primeLi:
        if prime(i):
            print(i)
            answer += 1
    return answer
