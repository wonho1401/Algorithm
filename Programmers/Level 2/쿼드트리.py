def solution(arr):
    answer = [0,0]
    k = len(arr)
    def recursion(i,j,k):
        digit = arr[i][j]
        for x in range(i,i+k):
            for y in range(j,j+k):
                if digit != arr[x][y]:
                    k //= 2
                    recursion(i,j,k)
                    recursion(i,j+k,k)
                    recursion(i+k,j,k)
                    recursion(i+k,j+k,k)
                    return
        answer[digit] +=1
    recursion(0,0,k)
    return answer
