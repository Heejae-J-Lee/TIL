def solution(people, limit):
    answer = 0
    
    people.sort()
    borts = []
    for person in people[::-1]:
        if len(borts) == 0:
            borts.append(person)
            continue
            
        if borts[-1] + person <= limit:
            borts.pop()
            answer += 1
        else:
            borts.append(person)
    answer += len(borts)
    
    return answer