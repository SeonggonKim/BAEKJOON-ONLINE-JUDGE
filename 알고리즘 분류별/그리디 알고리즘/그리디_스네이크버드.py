import sys

num, snake = map(int, sys.stdin.readline().split())
fruit = list(map(int, sys.stdin.readline().split()))
fruit.sort()

for i in fruit:
    if i <= snake:
        snake += 1

print(snake)