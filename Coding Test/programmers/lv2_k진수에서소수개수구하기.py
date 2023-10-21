def solution(n, k):
    answer = 0
    
    n_to_k = ""
    p_list = []
    
    while True:
        if n < k:
            n_to_k = str(n) + n_to_k
            break
        n_to_k = str(n%k) + n_to_k
        n = n // k
    
    p_list = n_to_k.split("0")
    
    while True:
        if '' not in p_list:
            break
        p_list.remove('')
        
    p_list = list(map(int, p_list))
    p_list.sort()
    
    prev_p = 2
    
    for p in p_list:
        if p == prev_p:
            answer += 1
        elif prev_p < p:
            limit = int(p**(1/2))
            fl = True
            for i in range(2, limit+1):
                if p % i == 0:
                    fl = False
                    break
            if fl:
                answer += 1
                
    return answer