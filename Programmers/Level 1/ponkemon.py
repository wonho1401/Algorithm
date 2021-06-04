def solution(nums):
    answer = 0
    get = int(len(nums)/2)
    li = set(nums)
    if get >= len(li):
        return len(li)
    elif get < len(li):
        return get
