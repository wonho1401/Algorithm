import re
from collections import Counter
def solution(s):
    answer = []
    s = re.sub("\{|\}","",s)
    li = Counter(list(s.split(",")))
    li = li.most_common()
    for i in range(len(li)):
        answer.append(int(li[i][0]))
    return answer
