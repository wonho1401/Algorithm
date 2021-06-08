def solution(n, arr1, arr2):
    answer = []
    res = []
    for i in range(n):
        res.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
    for i in range(len(res)):
        x=""
        for j in range(n):
            if res[i][j] == '1':
                x += "#"
            elif res[i][j] == '0':
                x += " "
        answer.append(x)
    return answer
