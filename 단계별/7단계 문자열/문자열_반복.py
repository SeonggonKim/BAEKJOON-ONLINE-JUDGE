import sys

n = int(sys.stdin.readline())

word = list(sys.stdin.readline().split() for _ in range(n))

for i in range(n):
    for j in range(len(word[i][1])):
        print(word[i][1][j] * int(word[i][0]), end='')
    print()