T = int(input())

for turn in range(1, T+1):
    N = int(input())
    graph = []
    for __ in range(N):
        graph.append(list(input()))
        # graph.append(list(map(int, input().split())))

    answer = 0

    start, end = N//2, N//2+1
    for i in range(N//2+1):
        for j in range(start, end):
            temp = int(graph[i][j])
            answer += temp
        start -= 1
        end += 1

    # 대칭 아래쪽 처리
    start, end = 1, N-1
    for i in range(N//2+1, N):
        for j in range(start, end):
            temp = int(graph[i][j])
            answer += temp
        start += 1
        end -= 1

    print(f'#{turn} {answer}')