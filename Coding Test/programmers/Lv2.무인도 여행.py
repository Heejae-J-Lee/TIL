dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def solution(maps):
    answer = []
    size = (len(maps), len(maps[0]))
    for row in range(size[0]):
        for col in range(size[1]):
            meals = 0
            st = [(row, col)]
            
            while len(st) != 0:
                r, c = st.pop()
                
                if maps[r][c] != "X":
                
                    meals += int(maps[r][c])
                    maps[r]= maps[r][:c]+'X'+maps[r][c+1:]
                    for i in range(4):
                        next_r = r + dr[i]
                        next_c = c + dc[i]
                        
                        if next_r < 0 or size[0] <= next_r or next_c < 0 or size[1] <= next_c:
                            continue
                        else:
                            st.append((next_r, next_c))
            
            if meals != 0:
                answer.append(meals)
    
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    
    return answer
