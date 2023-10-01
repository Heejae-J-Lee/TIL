def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n+1)]
    
    n_temp = 1
    
    for i in range(1, n):
        n_temp *= i
    
    for i in range(n-1, 0, -1):
        t = 0
        
        while True:
            if k > n_temp:
                t += 1
                k -= n_temp
            else:
                break
                

        t = numbers[t]
        n_temp //= i
        numbers.remove(t)
        answer.append(t)
        
    answer += numbers
    
    return answer
