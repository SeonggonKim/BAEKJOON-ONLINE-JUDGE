import sys
from collections import Counter

n = int(input())
test = list(map(int, sys.stdin.readline().split()))

m = int(input())
answer = list(map(int, sys.stdin.readline().split()))

counter = Counter(test)

for i in answer:
    print(counter[i], end = ' ')