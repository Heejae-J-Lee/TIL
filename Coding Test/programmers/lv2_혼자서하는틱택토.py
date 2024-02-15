def solution(board):
    answer = -1
    
    nums_OX = 0
    scores = [0,0]
    
    for line in board:
        nums_OX += line.count('O')
        nums_OX -= line.count('X')
        
        if line == "OOO":
            scores[0] += 1
        elif line == "XXX":
            scores[1] += 1
    
    for i in range(3):
        line = board[0][i] + board[1][i] + board[2][i]
        if line == "OOO":
            scores[0] += 1
        elif line == "XXX":
            scores[1] += 1
    
    if board[1][1] == "O":
        if board[0][0] + board[2][2] == "OO":
            scores[0] += 1
        if board[0][2] + board[2][0] == "OO":
            scores[0] += 1
    elif board[1][1] == "X":
        if board[0][0] + board[2][2] == "XX":
            scores[1] += 1
        if board[0][2] + board[2][0] == "XX":
            scores[1] += 1
    
    if nums_OX in [0, 1]:
        if min(scores) > 0:
            answer = 0
        elif scores[1] == 1 and nums_OX == 1:
            answer = 0
        elif scores[0] == 1 and nums_OX == 0:
            answer = 0
        else:
            answer = 1
    else:
        answer = 0
    
    return answer