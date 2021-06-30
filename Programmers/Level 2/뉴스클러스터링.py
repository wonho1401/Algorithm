from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    li1 = Counter([(str1[i]+str1[i+1]) for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha() == True])
    li2 = Counter([(str2[i]+str2[i+1]) for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha() == True])
    
    ints = 0
    for i in li1:
            if i in li2:
                ints += min(li1[i],li2[i])
    un = len(list(li1.elements())) + len(list(li2.elements())) - ints

    if un == 0:
        return 65536
    answer = int(f"{((ints / un) * 65536)}".split(".")[0])
    return answer
