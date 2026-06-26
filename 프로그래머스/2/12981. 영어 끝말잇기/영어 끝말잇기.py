def solution(n, words):
    answer = [0,0]
    
    stack = [words[0]]
    for idx, word in enumerate(words[1:]):
        if word in stack or stack[-1][-1] != word[0]:
            p = (idx+2) % n
            turn = (idx+2) // n
            if p != 0:
                turn += 1
            
            else:
                p = n
            
            answer[0] = p
            answer[1] = turn
            break
            
        else:
            stack.append(word)
    

    return answer