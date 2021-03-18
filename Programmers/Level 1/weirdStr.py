def solution(s):
    s= list(s)
    count = 0
    for i in range(len(s)):
        if s[i]== " ":
            count = 0
            continue
        if count % 2 == 0:
            s[i] = s[i].capitalize()
        else:
            s[i] = s[i].lower()
        count += 1
    return "".join(s)
  
  
