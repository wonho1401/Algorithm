def solution(n, lost, reserve):
    los = set(lost) - set(reserve)
    rsv = set(reserve) - set(lost)
    
    for i in rsv:
        if i-1 in los:
            los.remove(i-1)
        elif i+1 in los:
            los.remove(i+1)
            
    return n - len(los)
