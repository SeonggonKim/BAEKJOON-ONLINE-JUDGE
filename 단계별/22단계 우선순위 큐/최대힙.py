import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, -x)
    if len(heap) == 0 and x == 0:
        print(x)
    if len(heap) != 0 and x == 0:
        print(-heapq.heappop(heap))