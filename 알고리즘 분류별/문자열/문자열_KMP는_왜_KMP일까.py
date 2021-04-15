import sys
word = sys.stdin.readline().split('-')

first = []
for i in range(len(word)):
    first.append(word[i][0])

for i in range(len(first)):
    print(first[i], end='')