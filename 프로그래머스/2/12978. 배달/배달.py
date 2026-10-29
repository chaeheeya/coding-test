from collections import deque

def solution(N, road, K):
    
    graph = [[] for __ in range(N+1)]
    for r in road:
        n1, n2, w = r
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
        
        
    INF = 99999999
    path = [INF] * (N+1)
    visited = [False] * (N+1)
    
    queue = deque()
    queue.append(1)
    path[1] = 0
    
    while queue:
        current = queue.popleft()
        # print("current: ", current)
        
        for i in graph[current]:
            # print("i: ", i)
            if path[i[0]] > path[current] + i[1]:
                path[i[0]] = path[current] + i[1]
                # print("path: ", path)
                queue.append(i[0])
    answer = 0
    for num in path[1:]:
        if num <= K:
            answer += 1

    return answer