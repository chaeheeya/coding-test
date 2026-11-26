from collections import deque

T = int(input())
for __ in range(T):
    N, M = map(int, input().split())

    docs = deque([])
    for i, w in enumerate(list(map(int, input().split()))):
        docs.append((i, w))

    # docs.sort(key=lambda x:x[1])
    max_num = max([d[1] for d in docs])
    cnt = 1
    check = False

    while not check:
        # print('max_num: ', max_num)
        # print('docs: ', docs)
        # print()

        if docs[0][1] != max_num:
            temp = docs.popleft()
            docs.append(temp)
        else:
            if docs[0][0] == M:
                check = True
                print(cnt)
            else:
                cnt += 1
                docs.popleft()
                max_num = max([d[1] for d in docs])

