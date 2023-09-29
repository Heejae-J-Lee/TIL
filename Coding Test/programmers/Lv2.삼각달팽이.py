dr = [1, 0, -1]
dc = [0, 1, -1]

def solution(n):
    answer = []
    
    snail = [[0 for _ in range(i+1)] for i in range(n)]
    limit = 0
    direction = 0
    cur = 1
    loc = [0, 0]
    for i in range(1, n+1):
        limit += i
        
    while True:
        if cur > limit:
            break
        snail[loc[0]][loc[1]] = cur
        cur += 1
        next = (loc[0] + dr[direction], loc[1] + dc[direction])
        if next[0] < next[1] or next[0] >= n:
            direction = (direction + 1) % 3
        elif snail[next[0]][next[1]] != 0:
            direction = (direction + 1) % 3
        loc = [loc[0] + dr[direction], loc[1] + dc[direction]]
            
    for shell in snail:
        answer += shell
    
    return answer
