import re
def solution(dartResult):
    score = {"S": 1, "D": 2, "T": 3}
    opt = {"":1, "*":2, "#": -1}
    d = re.compile("(\d+)([SDT])([*#]?)")
    dl = d.findall(dartResult)
    for i in range(len(dl)):
        if dl[i][2] == "*" and i > 0:
            dl[i-1] *= 2
        dl[i] = int(dl[i][0])**score[dl[i][1]]*opt[dl[i][2]]
    return sum(dl)
