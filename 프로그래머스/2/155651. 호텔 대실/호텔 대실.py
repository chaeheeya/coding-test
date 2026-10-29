from collections import deque

def solution(book_time):
    
    
    for idx, time in enumerate(book_time):
        start = int(time[0].split(':')[0]) * 60 + int(time[0].split(':')[1])
        end = int(time[1].split(':')[0]) * 60 + int(time[1].split(':')[1]) + 10
        book_time[idx] = (start, end)
    
    book_time.sort(key=lambda x:x[0])
    # print(book_time)
    
    answer = 1
    using = []
    using.append(book_time[0][1])
    for time in book_time[1:]:
        start, end = time
        # print("start, end: ", start, end)
        
        room = using[0]
        # print("room: ", using[0])
        if start < room:
            answer += 1
        else:
            using.pop(0)

        using.append(end)
        using.sort()
        # print("using: ", using)      
    
    return answer