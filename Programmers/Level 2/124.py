num = "124"
def solution(n):
    if n <= 3:
        return num[n-1]
    else:
        q,r = divmod(n - 1,3)
        return solution(q) + num[r]
