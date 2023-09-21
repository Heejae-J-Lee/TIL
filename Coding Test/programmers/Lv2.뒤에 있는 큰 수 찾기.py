def solution(numbers):
    num_arr = [0 for _ in range(len(numbers))]
    num_arr[-1] = -1
    
    for i in range(2, len(numbers)+1):
        if numbers[-i] < numbers[-i+1]:
            num_arr[-i] = numbers[-i+1]
            continue
        elif numbers[-i] < num_arr[-i+1]:
            num_arr[-i] = num_arr[-i+1]
            continue
        
        cur = 2
        while cur != i:
            if numbers[-i] < num_arr[-i+cur]:
                num_arr[-i] = num_arr[-i+cur]
                
            cur+=1
        
        if num_arr[-i] == 0:
            num_arr[-i] = -1
            
    return num_arr
