import sys

n = int(sys.stdin.readline())

for _ in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)