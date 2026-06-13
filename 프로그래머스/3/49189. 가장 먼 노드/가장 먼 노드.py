from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for __ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)
    
    INF = 1000000
    path = [INF for __ in range(n+1)]
    # print(path)
    
    path[1] = 0
    queue = deque()
    queue.append(1)
    
    while queue:
        current = queue.popleft()
        # print('current: ', current)
        # print(graph[current])
        for i in graph[current]:
            if path[current] + 1 < path[i]:
                path[i] = path[current]+1
                queue.append(i)
                
                
        # print('queue: ', queue)
        
    # print(path)
    path.sort()
    max_num = path[-2]
    
    
    return path.count(max_num)