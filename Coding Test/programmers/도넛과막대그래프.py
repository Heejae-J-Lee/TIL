def solution(edges):
    answer = [0,0,0,0]
    
    n = 1
    node = 0
    nodes = set()
    edges_to = {}
    
    for edge in edges:
        node_from = edge[0]
        node_to = edge[1]
        
        if n < max(edge):
            n = max(edge)
        
        if node_from not in edges_to.keys():
            edges_to[node_from] = 1
        else:
            edges_to[node_from] += 1
        
        nodes.add(node_to)
    
    while True:
        node += 1
        
        if node > n:
            break
        
        if node not in edges_to.keys():
            answer[2] += 1
            continue
        
        if (answer[0] == 0) and (node not in nodes) and (edges_to[node] != 1):
            answer[0] = node
            continue
            
        if edges_to[node] == 2:
            answer[3] += 1
            continue
    
    answer[1] = edges_to[answer[0]] - answer[2] - answer[3]
    
    return answer