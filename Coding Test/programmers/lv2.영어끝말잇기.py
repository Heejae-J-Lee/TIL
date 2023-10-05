def solution(n, words):
    answer = []    
    
    last_letter = None
    order = 0
    used = []
    
    while True:
        if answer != []:
            break
        
        order += 1
        
        for i in range(n):
            
            if len(words) == 0:
                answer = [0,0]
                break
                
            word = words[0]
            words = words[1:]
            
            if word in used:
                answer = [i+1, order]
                break
            elif last_letter == None or word[0] == last_letter:
                last_letter = word[-1]
                used.append(word)
            else:
                answer = [i+1, order]
                break
                
            
    return answer
