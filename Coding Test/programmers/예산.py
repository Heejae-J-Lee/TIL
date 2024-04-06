def solution(d, budget):
    answer = 0
    
    used = 0
    d.sort()
    for requested in d:
        used += requested
        if budget < used:
            break
        else:
            answer += 1
    
    return answer