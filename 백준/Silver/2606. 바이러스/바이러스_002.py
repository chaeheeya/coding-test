from collections import deque

N = int(input()) # 컴퓨터 수
L = int(input())

graph = [[] for __ in range(N+1)]
for __ in range(L):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

queue = deque()
visited = [False] * (N+1)

queue.append(1)
visited[1] = True

answer = 0
while queue:
    current = queue.popleft()

    for node in graph[current]:
        if not visited[node]:
            answer += 1
            queue.append(node)
            visited[node] = True

print(answer)