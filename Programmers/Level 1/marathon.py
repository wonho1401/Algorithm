def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    for x,y in zip(participant,completion):
        if x != y:
            return x
    return participant.pop()
