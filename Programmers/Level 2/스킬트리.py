def solution(skill, skill_trees):
    answer = 0
    li = []
    for i in range(len(skill)):
        li.append(skill[i])
    for i in range(len(skill_trees)):
        idx = 0
        for j in skill_trees[i]:
            if j in li:
                print(skill_trees[i])
                if j == li[idx]:
                    idx += 1
                else:
                    break
            if j == skill_trees[i][-1]:
                answer += 1
            elif j not in li:
                continue
    return answer
