def solution(n, words):
    answer = []
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            answer.append([(i%n)+1,(i//n)+1])
    if len(answer) == 0:
        return [0,0]
    else:
        answer.sort(key=lambda x: x[1])
        return answer[0]
