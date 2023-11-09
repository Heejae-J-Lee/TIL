def solution(n, words):
    answer = []

    words_used = set()
    last = None
    
    for idx, word in enumerate(words):
        if last == None:
            words_used.add(word)
            last = word[-1]
            continue
        
        if word in words_used:
            answer = [idx%n+1, idx//n+1]
            break
            
        if last != word[0]:
            answer = [idx%n+1, idx//n+1]
            break
        else:
            words_used.add(word)
            last = word[-1]
    
    if len(answer) == 0:
        answer = [0, 0]
    
    return answer