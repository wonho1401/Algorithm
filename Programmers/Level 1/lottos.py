def solution(lottos, win_nums):
    dic={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []
    _max = lottos.count(0)
    _min = 0
    for win in win_nums:
        if win in lottos:
            _max += 1
            _min += 1
    return [dic[_max],dic[_min]]
