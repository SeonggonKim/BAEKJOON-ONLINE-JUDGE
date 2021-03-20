import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

total = 0

for i in range(len(cost)-1):
    if cost[i] > cost[i+1]:
        total += cost[i] * length[i]
    else:
        total += cost[i] * length[i]
        cost[i+1] = cost[i]

print(total)