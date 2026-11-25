R, C = map(int, input().split())
board = []
for __ in range(R):
    board.append(input())

words = []
# 가로 검사
for i in range(R):
    temp = board[i]
    word = ''
    for w in temp:
        if w != '#':
            word += w
        else:
            if len(word) > 1:
                words.append(word)
            word = ''

    if len(word) > 1:
        words.append(word)


# 세로 검사
for i in range(C):
    word = ''
    for j in range(R):
        if board[j][i] != '#':
            word += board[j][i]
        else:
            if len(word) > 1:
                words.append(word)
            word = ''

    if len(word) > 1:
        words.append(word)

words.sort()
print(words[0])