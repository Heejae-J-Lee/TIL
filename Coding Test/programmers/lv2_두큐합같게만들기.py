def solution(queue1, queue2):
    answer = -2
    
    queue = queue1 + queue2
    
    sum_queue = 0
    for item in queue:
        sum_queue += item
        
    if sum_queue % 2 != 0:
        answer = -1
    else:
        target_sum = sum_queue // 2
        
        sum_queue1 = 0
        for item in queue1:
            sum_queue1 += item
            
        l = 0
        r = len(queue1) - 1
        
        cnt = 0
        
        while True:
            if sum_queue1 == target_sum:
                answer = cnt
                break
            elif sum_queue1 < target_sum:
                r += 1
                if len(queue) <= r:
                    answer = -1
                    break
                sum_queue1 += queue[r]
            else:
                sum_queue1 -= queue[l]
                l += 1
                if r<l:
                    answer = -1
                    break
                
            cnt += 1
    
    return answer
