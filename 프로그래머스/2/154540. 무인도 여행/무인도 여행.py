from collections import deque

def solution(maps):
    
    maps = [list(s) for s in maps]
    N = len(maps) # y
    M = len(maps[0]) # x
    
    y = [1,-1,0,0]
    x = [0,0,-1,1]
    
    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X':
                
                cnt = int(maps[i][j])
                queue = deque()
                queue.append((i,j))
                maps[i][j] = 'X'
                
                while queue:
                    current_y, current_x = queue.popleft()
                    for idx in range(4):
                        dy = current_y + y[idx]
                        dx = current_x + x[idx]
                        
                        if 0<=dx<M and 0<=dy<N and maps[dy][dx] != 'X':
                            queue.append((dy,dx))
                            cnt += int(maps[dy][dx])
                            maps[dy][dx] = 'X'
                            
                answer.append(cnt)
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)  
    
    return answer