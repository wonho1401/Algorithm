def solution(n):
    s=list(str(n))
    s.reverse()
    for i in range(len(s)):
        s[i]=int(s[i])
    return s
