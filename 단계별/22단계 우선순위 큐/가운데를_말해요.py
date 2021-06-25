import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    x = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    if min_heap and min_heap[0] < -max_heap[0]:
        max = -heapq.heappop(max_heap)
        min = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min)
        heapq.heappush(min_heap, max)

    print(-max_heap[0])