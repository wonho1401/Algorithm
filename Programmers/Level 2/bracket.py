def solution(s):
    li = list(s)
    stack = []
    answer = True
    for i in li:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                answer = False
                break
            elif stack[-1] == "(":
                stack.pop()
    if answer == True and len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer
