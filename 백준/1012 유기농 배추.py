from collections import deque

## 실제 제출용
# T = int(input()) # 테스트 케이스 개수 -> 이만큼 돌아서 테스트 하면 됨
# M, N, K = map(int, input().split()) # 가로, 세로, 배추가 포함된 칸 개수


## 테스트 용
T = 2
M, N, K = 10, 8, 17

# 1. 배추가 심어진 칸 먼저 그리기
G = [[0 for __ in range(M)] for __ in range(N)] # 이중리스트 -> 배추가 심어진 칸 표시
# print(G)

X = []
Y = []
for __ in range(K): #  실제로 G에 그림 그리기
    x, y = map(int, input().split()) # 실제로 사용할 것
    G[y][x] = 1
    X.append(x)
    Y.append(y)
# print(G)

# 2. 배추밭 탐색하기
def dfs(x, y):
    # 상하좌우 순으로 탐색함
    dx = [0, 0, -1, 1] # 왼쪽 오른쪽 움직이기
    dy = [1, -1, 0, 0] # 위 아래 움직이기

    queue = deque()
    queue.append((x, y))
    # print(queue)

    while queue:
        location = queue.popleft() # 현재 탐색하는 곳
        print(location)
        if G[location[1]][location[0]] != -1:
            G[location[1]][location[0]] = -1 # 탐색을 한번 하면 더 이상 하지 못하도록 처리

            for i in range(4):
                nx, ny = location[0]+dx[i], location[1]+dy[i]
                # print(ny, nx)

                if nx < 0 or nx >= M or ny < 0 or ny >= N: # 실제 범위를 침범하는 경우는 예외 처리
                    continue
                # print(ny, nx)

                if G[ny][nx] == 1: # 연장해서 탐색할 곳이 있는지 확인
                    queue.append((nx,ny))
                    # print("queue update: ", queue)

count = 0
for x in range(M):
    for y in range(N):
        if G[y][x] == 1:
            dfs(x, y)
            count += 1

print(count)

'''
[문제 풀면서 헷갈린 부분 & 준비할 부분]

1. 좌표 문제가 나올 경우: x/y 역할부터 고정
(x, y) : 좌표 넣는 순서
x = 가로 = 열 = column = M ( 0 <= ㅌ < M ) # index error 조심
y = 세로 = 행 = row = N (0 <= y < N )
grid[y][x]: grid 접근 방법

2. BFS/DFS는 "방문 처리 타이밍" 이 생몀임!
- pop한 다음 방문 처리할 경우, 이미 순회하면서 queue에 들어갔을 수 있음
- 그렇기 때문에, 큐에 넣는 순간 방문 처리하는 것이 필요함! 
    어차피 방문예정이기 때문에 중복 방문처리할 필요가 없어짐
- 방문 처리 타이밍 처리할때는 visited 배열을 따로 쓰는 것이 안전할수 있음

3. DFS/BFS 시작 조건을 무조건 걸기!
- 오늘 문제풀때는 모든 좌표에서 dfs를 호출했음. (방문 여부 확인 안함)
- 이렇게 할 경우, 이미 방문한 좌표인데, 또다시 탐색할 수 있음.
- 그렇기 때문에, 방문하지 않은 경우!! 에 탐색을 시작하는 것으로 조건을 걸어주는 것이 필요함

4. 배열 크기 키워서 덮으려고 하지 말기
- index error 난다고 무작정 배열 키우지 말기
- 대신에, 배열 크기를 문제에서 준 그대로, 범위 체크를 저오학하게 하자!
- 특히 좌표 문제일 경우, 상한선이 어디까지인지 체크를 제대로 해야함 (nx > M-1 .. X -> nx >= M)
    현재 입력으로 주어진 상한선이 무엇을 의미하는 것인지 생각 제대로 하기
'''