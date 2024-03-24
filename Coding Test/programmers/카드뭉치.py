def solution(cards1, cards2, goal):
    answer = 'Yes'
    p1 = 0
    p2 = 0
    
    for word in goal:
        if p1 < len(cards1) and cards1[p1] == word:
            p1 += 1
            continue
        elif p2 < len(cards2) and cards2[p2] == word:
            p2 += 1
            continue
        else:
            answer = "No"
            break
    return answer