def solution(land):
    for j in range(1,len(land)):
            for i in range(4):
                land[j][i]+=max(land[j-1][:i]+land[j-1][i+1:])
    return max(land[-1])
