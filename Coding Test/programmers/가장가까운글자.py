def solution(s):
    answer = []
    
    for idx, c in enumerate(s):
        order = -1
        for i in range(idx-1, -1, -1):
            if (c == s[i]) :
                order = idx-i
                break
        answer.append(order)
    
    return answer
