def solution(n, times):
    answer = 0
    
    l = 0
    r = times[0] * n
    
    while (l <= r):
        T = (l + r) // 2
        
        people = 0
        for time in times:
            people += (T) // time
        
        if people < n:
            l = T + 1
        elif people >= n:
            answer = T
            r = T - 1 
    
    return answer
