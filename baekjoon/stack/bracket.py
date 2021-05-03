n = int(input())
for _ in range(n):
    x = list(input())
    while len(x) != 0:
        if x[0] == ")":
            print("NO")
            break
        else:
            if ")" in x:
                x.remove(")")
                x.remove("(")
            else:
                print("NO")
                break
    if len(x) == 0:
        print("YES")
    
