from collections import deque

def solution(maps):
    
    
    queue = deque()
    queue.append((0, 0, 1))
    maps[0][0] = 0
    
    while queue:
        current = queue.popleft()

        print(current)
        
        if current[1] == len(maps[0])-1 and current[0] == len(maps)-1:
            return current[2]
        
        distance = current[2]
        
        x = [0, 0, -1, 1]
        y = [1, -1, 0, 0]
        
        for i in range(4):
            dx = current[1] + x[i]
            dy = current[0] + y[i]
            
            if 0 <= dx < len(maps[0]) and 0<= dy < len(maps) and maps[dy][dx] != 0:
                queue.append((dy, dx, distance+1))
                maps[dy][dx] = 0
    
    return -1