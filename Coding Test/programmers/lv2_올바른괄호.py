def solution(s):
    answer = True
    
    n = 0
    
    for c in s:
        if c == '(':
            n += 1
        elif c == ')':
            if n == 0:
                return False
            n -= 1

    if n != 0:
        return False
    
    return True