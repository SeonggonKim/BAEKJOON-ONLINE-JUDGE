import sys

n = int(input())
number = list(map(int, sys.stdin.readline().split()))
set_number = set(number)
answer = sorted(set_number)

count = {}
for i in range(len(answer)):
    count[answer[i]] = i

for i in range(n):
    print(count[number[i]], end=' ')