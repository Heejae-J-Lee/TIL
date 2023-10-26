def dfs(k, dungeons, depth):
    max_depth = depth
    for i, dungeon in enumerate(dungeons):
        if k < dungeon[0]:
            continue
            
        rest = dungeons.copy()
        rest.pop(i)
        d = dfs(k-dungeon[1], rest, depth+1)
        max_depth = max(max_depth, d)
    return max_depth

def solution(k, dungeons):
    answer = -1
    answer = dfs(k,dungeons, 0)
    return answer