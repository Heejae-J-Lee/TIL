dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turning(board, queries):
    
    x1 = queries[0] - 1
    y1 = queries[1] - 1
    x2 = queries[2] - 1
    y2 = queries[3] - 1
    x, y = x1, y1
    
    tps = [(x1,y2),(x2,y2),(x2,y1),(x1,y1)]
    
    d = 0
    
    prev_val = board[x][y]
    min_val = prev_val
    last_tunring_val = board[x+1][y]
    while d < 4:
        if tps[d][0] == x and tps[d][1] == y:
            d += 1
            
        if d >= 4:
            break
        
        next_x = x + dx[d]
        next_y = y + dy[d]
        
            
        next_val = board[next_x][next_y]
        board[next_x][next_y] = prev_val
        
        if next_val < min_val:
            min_val = next_val
        prev_val = next_val
        
        x = next_x
        y = next_y
    board[x1][y1] = last_tunring_val
    
    return min_val
    

def solution(rows, columns, queries):
    answer = []
    
    board = [[row * columns + (column + 1) for column in range(columns)] for row in range(rows)]
            
    for querie in queries:
        answer.append(turning(board, querie))
        
    return answer