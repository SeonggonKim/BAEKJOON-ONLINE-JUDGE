import sys
n = int(sys.stdin.readline())
result = list(list(sys.stdin.readline().strip()) for _ in range(n))

for i in range(n):
    score = 0
    count = 1
    for j in range((len(result[i]))):
        if result[i][j] == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)