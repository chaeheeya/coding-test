from collections import deque

def solution(priorities, location):
    
    temp = deque()
    for idx, prior in enumerate(priorities):
        temp.append((idx, prior))
    
    
    result = []
    while temp:
        current = temp.popleft()
        print('current: ', current)
        
        higher_prior = False
        for i in temp:
            if i[1] > current[1]:
                higher_prior = True
        
        if higher_prior:
            temp.append(current)
        else:
            result.append(current[0])
            if current[0] == location:
                break             
        
    
    return len(result)