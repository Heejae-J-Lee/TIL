def solution(s):
    answer = ''
    
    first_letter = True
    
    for c in s:
        if c == ' ':
            first_letter = True
            answer += c
        elif first_letter:
            answer += c.upper()
            first_letter = False
        else:
            answer += c.lower()
    
    return answer