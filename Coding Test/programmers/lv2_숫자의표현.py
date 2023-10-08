def solution(n):
    answer = 0
    
    num_array = []
    cur = 0
    l, r = 0, 0 
    
    for i in range(n+1):
        cur += i
        num_array.append(cur)
    
    while True:
        if l == len(num_array)-1:
            break
            
        counter = num_array[r] - num_array[l]
        
        if counter < n:
            r += 1
        elif n < counter:
            l += 1
        else:
            l += 1
            answer += 1
    
    return answer
