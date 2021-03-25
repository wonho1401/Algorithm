def solution(n):
    answer = 0

    li = list(str(n))
    for i in range(len(li)):
        li[i] = int(li[i])
    answer = sum(li)

    return answer
