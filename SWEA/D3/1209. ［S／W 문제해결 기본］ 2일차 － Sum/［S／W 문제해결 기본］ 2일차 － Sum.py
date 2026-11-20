N = 100
T = 10

for __ in range(T):
    turn = int(input())
    graph = []
    for __ in range(N):
        graph.append(list(map(int, input().split())))

    max_num = 0
    # 가로
    for i in range(N):
        if sum(graph[i]) > max_num:
            max_num = sum(graph[i])

    # 세로
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(graph[j][i])
        if sum(temp) > max_num:
            max_num = sum(temp)

    # 오른쪽 대각선
    temp = []
    for i in range(N):
        temp.append(graph[i][i])
    if sum(temp) > max_num:
        max_num = sum(temp)

    # 왼쪽 대각선
    temp = []
    for i in range(N):
        temp.append(graph[i][N-i-1])
    if sum(temp) > max_num:
        max_num = sum(temp)

    print(f'#{turn} {max_num}')