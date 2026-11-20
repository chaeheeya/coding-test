N = int(input())
words = []
for __ in range(N):
    words.append(list(input()))

answer = 0
for word in words:
    alphabet = list(set(word))

    stack = []
    for w in word:
        if not stack:
            stack.append(w)
            alphabet.remove(w)
        else:
            if w in alphabet:
                alphabet.remove(w)
                stack.append(w)
            elif stack[-1] == w:
                stack.append(w)

    if stack == word:
        answer += 1

print(answer)





