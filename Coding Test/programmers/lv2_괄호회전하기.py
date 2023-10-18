def solution(s):
    answer = 0
    open_brackets = '({['
    close_brackets = ')}]'
    dict_brackets = {"(":")", "{":"}","[":"]",")":"(","}":"{","]":"["}
    
    new_ss = []
    fl_word = True
    
    for i, c in enumerate(s):
        if fl_word and c in open_brackets:
            new_ss.append(s[i:] + s[:i])
            fl_word = False
        if c in close_brackets:
            fl_word = True
    
    for new_s in new_ss:
        if answer != 0:
            break
        st = []
        
        for c in new_s:
            if c in open_brackets:
                st.append(c)
            else:
                size_st = len(st)
                
                if size_st == 0:
                    answer = 0
                    break
                    
                last_c = st.pop()
                
                if dict_brackets[c] != last_c:
                    answer = 0
                    break
                elif size_st == 1:
                    answer += 1
    
    return answer