dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(land):
    answer = 0
    
    depth = len(land)
    size = len(land[0])
    
    amount_of_oil = [0 for _ in range(size)]
        
    for i in range(size):
        for j in range(depth):
            rows = set()
            next_blocks = []
            oils = 0
            if land[j][i] != 0:
                next_blocks.append((j,i))
                land[j][i] = 0
                rows.add(i)
                oils += 1
            
            while (len(next_blocks)!=0):
                block = next_blocks[0]
                next_blocks.pop(0)
                
                for d in range(4):
                    next_row = block[1] + dx[d]
                    next_depth = block[0] + dy[d]
                    
                    if next_row < 0 or size <= next_row or next_depth < 0 or depth <= next_depth:
                        continue
                    
                    if land[next_depth][next_row] != 0:
                        next_blocks.append((next_depth,next_row))
                        land[next_depth][next_row] = 0
                        rows.add(next_row)
                        oils += 1
            for row in rows:
                amount_of_oil[row] += oils
    
    answer = max(amount_of_oil)
    
    return answer
