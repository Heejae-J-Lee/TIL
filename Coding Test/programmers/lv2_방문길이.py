operations = ['U', 'L', 'D', 'R']
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def solution(dirs):
    answer = 0
    map = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    y = 5
    x = 5
    
    for dir in dirs:
        d = operations.index(dir)
        
        new_y = y + dy[d]
        new_x = x + dx[d]
        if (new_y < 0) or (new_y > 10) or(new_x < 0) or (new_x > 10):
            continue
        
        rev_d = (d+2) % 4
        if map[y][x][d] == 0:
            map[y][x][d] = 1
            map[new_y][new_x][rev_d] = 1
            answer += 1
        
        # update location
        y = new_y
        x = new_x
        
    return answer