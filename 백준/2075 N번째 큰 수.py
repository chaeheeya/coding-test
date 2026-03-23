import heapq
import sys

N = int(input())
heap = []

for __ in range(N):
    heapq.heapify(heap)
    _input = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    for i in _input:
        heapq.heappush(heap, i)
    # print(heap)
    heap = heapq.nlargest(N, heap)

print(heap[-1])