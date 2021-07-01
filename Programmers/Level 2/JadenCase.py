import re
def solution(s):
    answer = ''
    s = s.lower()
    s = s[0].upper()+s[1:]
    tmp = re.findall(' +\w', s)

    for i in tmp:
        s = s.replace(i,i.upper())
    return s
