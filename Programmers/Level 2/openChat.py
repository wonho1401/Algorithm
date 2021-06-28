def solution(record):
    answer = []
    dic = {}
    for rec in record:
        temp = rec.split()
        if len(temp) == 3:
            cmd, uid, nickname = temp[0],temp[1],temp[2]
        elif len(temp) == 2:
            cmd, uid = temp[0], temp[1]
        if cmd == "Enter" or cmd == "Change":
            dic[uid] = nickname
    for rec in record:
        temp = rec.split()
        if len(temp) == 3:
            cmd, uid, nickname = temp[0],temp[1],temp[2]
        elif len(temp) == 2:
            cmd, uid = temp[0], temp[1]
        if cmd == "Enter":
            answer.append(f"{dic[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{dic[uid]}님이 나갔습니다.")
    return answer
