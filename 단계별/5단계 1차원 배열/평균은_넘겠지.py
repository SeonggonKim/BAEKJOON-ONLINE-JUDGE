import sys

n = int(sys.stdin.readline())

test = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

for i in range(n):
    count = 0
    for j in range(1, test[i][0]+1):
        if test[i][j] > (sum(test[i]) - test[i][0]) / test[i][0]:
            count += 1
    print('%.3f' %(round(count / test[i][0] * 100, 3)), '%', sep = '')