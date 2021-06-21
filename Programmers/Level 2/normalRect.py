def gcd(w,h):
    while h:
        w,h = h, w%h
    return w
def solution(w,h):
    return w*h - (w+h - gcd(w,h))
