dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

def hw_check(hw, n):
    in_board = True
    if hw < 0 or n <= hw:
        in_board = False
    return in_board
        
def solution(board, h, w):
    answer = 0
    
    n = len(board)
    
    selected_color = board[h][w]
    
    for direction in range(4):
        next_h = h + dh[direction]
        next_w = w + dw[direction]
        if hw_check(next_h, n) and hw_check(next_w, n):
            if board[next_h][next_w] == selected_color:
                answer += 1                
        else:
            continue
            
    return answer
