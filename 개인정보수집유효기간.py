def solution(today, terms, privacies):
    answer = []
    
    today_year, today_month, today_day = map(int, today.split('.'))
    
    #print(today_year, today_month, today_day)
        
    dict_terms = {}
    for term in terms:
        name, duration = term.split()
        dict_terms[name] = int(duration)
    
    for idx, privacy in enumerate(privacies):
        date, term_name = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        year = year + (month + dict_terms[term_name] - 1) // 12
        month = (month + dict_terms[term_name] - 1) % 12 + 1
        
        if 1 < day:
            day -= 1
        else:
            month -= 1
            day = 28
            
            if month == 0:
                month = 12 
                year -= 1
        
        #print(year, month, day)
        if (year < today_year) or (year == today_year and (month < today_month or (month == today_month and day < today_day))):
            answer.append(idx+1)
    
    return answer
