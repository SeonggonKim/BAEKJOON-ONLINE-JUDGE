import sys
case = []

while True:
    case.append(list(map(int, sys.stdin.readline().split())))
    if case[-1] == [0, 0, 0]:
        break

result = []

for i in range(len(case)-1):
    start_point = 0
    count = 0
    while True:
        start_point += case[i][1]
        if start_point > case[i][2] and (case[i][2] % case[i][1] < case[i][0]):
            count += (case[i][2] % case[i][1])
            result.append(count)
            break
        elif start_point > case[i][2] and (case[i][2] % case[i][1] >= case[i][0]):
            count += case[i][0]
            result.append(count)
            break
        else:
            count += case[i][0]

for i in range(len(result)):
    print('Case ' + str(i+1) + ': ' + str(result[i]))
