T = int(input())

for turn in range(1, T+1):
    N, M = map(int, input().split())

    land = []
    for __ in range(N):
        land.append(list(map(int, input().split())))

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    answer = 0
    for i in range(N):
        for j in range(M):
            current = land[i][j]
            # print('current: ', current, i, j)
            cnt = 0

            for y, x in zip(dy, dx):
                # print('i+y, j+x:', i+y, j+x)
                if 0 <= i+y < N and 0 <= j+x < M and land[i+y][j+x] < current:
                    cnt += 1
                    # print('cnt: ', cnt)

            if cnt >= 4:
                answer += 1
    print(f'#{turn} {answer}')


