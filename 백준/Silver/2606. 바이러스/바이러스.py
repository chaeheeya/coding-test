'''
- 구해야하는 것: 1번에서부터 연결된 컴퓨터 수 (count)
- 자료구조: BFS
'''
from collections import deque


N = int(input())
E = int(input())

graph = [[0] for __ in range(N+1)]
# print(graph)

for __ in range(E):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
queue = deque()
queue.append(1)
visited[1] = True

count = 0
while queue:
    node = queue.popleft()

    for n in graph[node]:
        if not visited[n] and n != 0:
            queue.append(n)
            visited[n] = True
            count += 1

print(count)