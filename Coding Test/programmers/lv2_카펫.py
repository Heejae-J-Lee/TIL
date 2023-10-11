def solution(brown, yellow):
    answer = []
    
    tiles = brown + yellow
    c = 3
    
    while True:
        if (tiles % c) == 0:
            r = tiles // c
            
            if (r-2)*(c-2) == yellow:
                answer = [r,c]
                break
        c += 1
    return answer