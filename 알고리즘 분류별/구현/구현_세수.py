import sys
number = list(map(int, sys.stdin.readline().split()))
number.sort(reverse=True)
print(number[1])