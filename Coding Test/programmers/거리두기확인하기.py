def solution(places):
    answer = []
    
    for place in places:
        candidates = []
        isolated = 1
        
        for r in range(len(place)):
            for c in range(len(place[0])):
                if place[r][c] == 'P':
                    candidates.append([r,c])
                
        for idx, candidate1 in enumerate(candidates):
            for candidate2 in candidates[idx+1:]:
                dist = abs(candidate1[0] - candidate2[0]) + abs(candidate1[1] - candidate2[1])
            
                if dist == 1:
                    isolated = 0
                    break
                elif dist == 2:
                    if candidate1[0] == candidate2[0] or candidate1[1] == candidate2[1]:
                        r = (candidate1[0] + candidate2[0]) // 2
                        c = (candidate1[1] + candidate2[1]) // 2
                        if place[r][c] != "X":
                            isolated = 0
                            break
                    else:
                        r = min(candidate1[0], candidate2[0])
                        c = min(candidate1[1], candidate2[1])
                        
                        if place[r][c] == "P":
                            if place[r+1][c] != "X" or place[r][c+1] != "X":
                                isolated = 0
                                break
                        else:
                            if place[r][c] != "X" or place[r+1][c+1] != "X":
                                isolated = 0
                                break
                                
                    
        
        answer.append(isolated)
            
    return answer