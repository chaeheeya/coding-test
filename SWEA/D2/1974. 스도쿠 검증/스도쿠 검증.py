T = int(input())
for turn in range(1, T+1):

    graph = []
    for __ in range(9):
        graph.append(list(map(int, input().split())))
    # print(graph)

    answer = 1
    # 가로 검사
    for i in range(9):
        # print(f'{i+1}번째')
        temp = []
        for j in range(9):
            temp.append(graph[i][j])
        temp.sort()
        # print('temp: ', temp)
        check = 1
        for num in temp:
            # print('num, check: ', num, check)
            if num != check:
                answer = 0
                break
            else:
                check += 1
        # print('answer: ', answer)

        if answer == 0:
            break
    #
    # # 세로 검사
    if answer != 0:
        # print('세로 검사 시작')
        for i in range(9):
            # print(f'{i+1}번째')
            temp = []

            for j in range(9):
                temp.append(graph[j][i])

            # print('temp: ', temp)
            temp.sort()
            # print('temp: ', temp)
            check = 1
            for num in temp:
                # print('num, check: ', num, check)
                if num != check:
                    answer = 0
                    break
                else:
                    check += 1
            # print('answer: ', answer)

            if answer == 0:
                break

    # 정사각 검사
    if answer != 0:
        for sy in range(0, 9, 3):
            for sx in range(0, 9, 3):

                temp = []

                for i in range(sy, sy + 3):
                    for j in range(sx, sx + 3):
                        temp.append(graph[i][j])

                # print(temp)
                temp.sort()
                # print('temp: ', temp)
                check = 1
                for num in temp:
                    # print('num, check: ', num, check)
                    if num != check:
                        answer = 0
                        break
                    else:
                        check += 1
                # print('answer: ', answer)

                if answer == 0:
                    break
            if answer == 0:
                break

    print(f'#{turn} {answer}')
