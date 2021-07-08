def solution(s):
    zeroCnt = 0
    cnt = 0
    while len(s) > 1:
        zeroCnt += s.count("0")
        s = format(len(s) - s.count("0"),"b")
        cnt += 1
    return [cnt,zeroCnt]
