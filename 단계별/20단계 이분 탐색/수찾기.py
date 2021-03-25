import sys

n = int(input())
test = list(map(int, sys.stdin.readline().split()))

m = int(input())
answer = list(map(int, sys.stdin.readline().split()))

correct = [0 for _ in range(m)]
for i in range(m):
    if answer[i] in test:
        correct[i] = 1

for i in correct:
    print(i)