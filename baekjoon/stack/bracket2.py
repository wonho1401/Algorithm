while True:
    s = input()
    if s == ".":
        break
    stack =[]
    flag = 1
    for i in s:
        if i == "[" or i =="(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 or stack[-1] == "[":
                flag = 0
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if len(stack) == 0 or stack[-1] == "(":
                flag = 0
                break
            elif stack[-1] == "[":
                stack.pop()
    if flag == 1 and len(stack) == 0 :
        print("yes")
    else:
        print("no")
        
