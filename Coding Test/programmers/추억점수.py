def solution(name, yearning, photo):
    answer = []
    point_longing = {}

    for person, score in zip(name, yearning):
        point_longing[person] = score
    
    for people in photo:
        point = 0
        for person in people:
            if person not in point_longing.keys():
                continue
            point += point_longing[person]
            
        answer.append(point)
    
    return answer
