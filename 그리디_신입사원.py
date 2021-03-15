import sys

t = int(input())

for i in range(t):
    n = int(input())
    score = []
    count = 1
    for j in range(n):
        score.append(list(map(int, sys.stdin.readline().split())))

    score.sort(key = lambda x: (x[0]))
    max = score[0][1]

    for k in range(1, n):
        if max > score[k][1]:
            count += 1
            max = score[k][1]
    print(count)