def solution(numbers, target):
    answer = 0
    
    result = [0]
    for n in numbers:
        temp = []
        while result:
            current = result.pop()
            temp.append(current+n)
            temp.append(current+(-1*n))
        result = temp
    
    # print(result)
    for r in result:
        if r == target:
            answer += 1
    
    return answer