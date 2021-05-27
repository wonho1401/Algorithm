def solution(s):
    li = s.split(" ")
    li = list(map(int,li))
    mm = [min(li),max(li)]
    return " ".join(map(str,mm))
