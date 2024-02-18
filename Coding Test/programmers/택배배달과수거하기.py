def solution(cap, n, deliveries, pickups):
    answer = 0
    
    ptr_deliveries = n-1
    ptr_pickups = n-1
    
    while True:
        if ptr_deliveries == -1 and ptr_pickups == -1:
            break
        
        dist = 0
        flag_first_point = True
        
        if ptr_deliveries != -1:
            num_deliveries = 0
            
            while True:
                if num_deliveries == cap or ptr_deliveries == -1:
                    break
                
                if deliveries[ptr_deliveries] == 0:
                    ptr_deliveries -= 1
                else:
                    if flag_first_point:
                        dist = ptr_deliveries + 1
                        flag_first_point = False
                    deliveried_item = min(cap-num_deliveries, deliveries[ptr_deliveries])
                    num_deliveries +=  deliveried_item
                    deliveries[ptr_deliveries] -= deliveried_item
        
        flag_first_point = True
        
        if ptr_pickups != -1:
            num_pickups = 0
                
            while True:
                if num_pickups == cap or ptr_pickups == -1:
                    break
                
                if pickups[ptr_pickups] == 0:
                    ptr_pickups -= 1
                else:
                    if flag_first_point:
                        dist = max(dist, ptr_pickups + 1)
                        flag_first_point = False
                    empty_boxes = min(cap-num_pickups, pickups[ptr_pickups])
                    num_pickups +=  empty_boxes
                    pickups[ptr_pickups] -= empty_boxes
        
        answer += dist * 2
            
    return answer