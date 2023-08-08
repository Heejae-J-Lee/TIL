def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    cur = -1
    
    for target in targets:
        if target[0] <= cur and cur < target[1]:
            continue
        cur = target[1]-1
        answer += 1
        
    return answer