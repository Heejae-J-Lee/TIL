def solution(storey):
    answer = 0
    
    while True:
        if storey == 0:
            break
        ones = storey % 10
        storey = storey // 10
        
        if ones == 5:
            if storey % 10 < 5:
                answer += ones
            else:
                answer += (10-ones)
                storey += 1
        elif ones < 5:
            answer += ones
        else:
            answer += (10-ones)
            storey += 1
        
    return answer
