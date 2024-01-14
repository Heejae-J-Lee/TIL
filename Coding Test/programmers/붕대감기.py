def solution(bandage, health, attacks):
    answer = -1
    
    cur_time = 0
    cur_health = health
    
    for attack in attacks:
        
        count_bandage_success = (attack[0] - 1) - cur_time
        cur_time = attack[0]
        
        cur_health = min(health, cur_health + count_bandage_success * bandage[1] + (count_bandage_success // bandage[0] * bandage[2]))
        
        cur_health = cur_health - attack[1]
                                         
        if cur_health <= 0:
            break
    
    if 0 < cur_health:
        answer = cur_health
    
    return answer
