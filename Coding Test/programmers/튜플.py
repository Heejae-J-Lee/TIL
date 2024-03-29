def solution(s):
    answer = []
    
    subsets = s[2:].replace('"','')
    subsets = subsets.replace('}','')
    subsets = subsets.split(',{')
    subsets.sort(key = lambda x : len(x))
    
    prev_elements = set()
    for subset in subsets:
        elements = set(map(int,subset.split(',')))
        answer.append(list(elements - prev_elements)[0])
        prev_elements = elements.copy()
        
    return answer
