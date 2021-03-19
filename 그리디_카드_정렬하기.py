import sys
import heapq

n = int(sys.stdin.readline())
number = []

for i in range(n):
    heapq.heappush(number, int(sys.stdin.readline()))

answer = 0
for i in range(n-1):
    a = heapq.heappop(number)
    b = heapq.heappop(number)
    heapq.heappush(number, a+b)
    answer += a+b
print(answer)