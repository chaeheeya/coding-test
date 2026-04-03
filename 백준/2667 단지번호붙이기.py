from collections import deque

N = int(input())
picture = []

for __ in range(N):
    temp = [int(i) for i in input()]
    picture.append(temp)

# print(picture)
queue = deque()

x = [-1, 1, 0, 0]
y = [0, 0, 1, -1]

result = []
for i in range(N):
    for j in range(N):
        if picture[i][j] == 1:
            # print('현재 시작 위치: ', i, j)
            count = 1
            queue.append((i, j))
            picture[i][j] = 0
            while queue:
                # print('stack 시작 전: ', stack)
                current = queue.popleft()
                for idx in range(4):
                    nx = current[1] + x[idx]
                    ny = current[0] + y[idx]

                    if 0 <= nx < N and 0 <= ny < N and picture[ny][nx] == 1:
                        queue.append((ny, nx))
                        # print('stack 시작 후: ', stack)
                        count += 1
                        picture[ny][nx] = 0
            result.append(count)
            # print(all)


print(len(result))
result.sort()
for i in result:
    print(i)