import sys
number = list(list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline())))

for i in range(len(number)):
    print(number[i][0]+number[i][1])