import sys

n = int(sys.stdin.readline())

check_list = [0] * 10000

for i in range(n):
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num] + 1

for i in range(10000):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)