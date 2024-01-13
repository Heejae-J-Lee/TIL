def solution(k, m, score):
    answer = 0
    
    score.sort()
    score.reverse()
    n = m-1
    
    while True:
        if len(score) <= n:
            break
        answer += score[n] * m
        n += m
    
    return answer
