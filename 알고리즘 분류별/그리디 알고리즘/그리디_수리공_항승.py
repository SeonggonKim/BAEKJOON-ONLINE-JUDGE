import sys

N, L = map(int, sys.stdin.readline().split())
hole = list(list(map(int, sys.stdin.readline().split())))
hole.sort()

start = 0
cnt = 0
for i in hole:
    if start < i:
        start = i + L - 1
        cnt += 1

print(cnt)