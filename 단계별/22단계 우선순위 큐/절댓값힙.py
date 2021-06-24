import sys
import heapq

heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    if x == 0 and len(heap) != 0:
        out = heapq.heappop(heap)
        print(out[1])
    elif x == 0 and len(heap) == 0:
        print(x)