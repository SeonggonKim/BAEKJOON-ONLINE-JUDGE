number = list(int(input()) for i in range(3))

mul = list(str(number[0] * number[1] * number[2]))

result = [0 for _ in range(10)]

for i in range(len(mul)):
    for j in range(10):
        if int(mul[i]) == j:
            result[j] += 1

for i in result:
    print(i)
