import math
def solution(n,a,b):
    while True:
        if n == 1:
            return 1
        if (a <= n //2 and b > n //2 ) or (a > n//2 and b <= n //2):
            return int(math.log2(n))
        elif a <= n // 2 and b <= n //2 :
            n //=2
        elif a > n // 2 and b > n // 2 :
            if a == n:
                a = n//2
                n //= 2
                b = b % n
            elif b == n:
                b = n//2
                n //= 2
                a = a % n
            else:  
                n //= 2
                a = a % n
                b = b % n
