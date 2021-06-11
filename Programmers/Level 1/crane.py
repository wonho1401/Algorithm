def solution(board, moves):
    answer = 0
    temp = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] == 0:
                continue
            if board[i][move-1] > 0:
                temp.append(board[i][move-1])
                board[i][move-1] = 0
                break
        for i in range(1,len(temp)):
            if temp[i-1] == temp[i]:
                del temp[i]
                del temp[i-1]
                answer += 2
    return answer
