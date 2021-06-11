def solution(left, right):
    li = list(range(left,right+1))
    answer = 0

    for i in li:
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        elif cnt % 2 == 1:
            answer -= i
    return answer
