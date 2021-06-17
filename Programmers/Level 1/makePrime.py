from itertools import combinations
import math

def prime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if prime(sum(i)):
            answer += 1
    return answer
