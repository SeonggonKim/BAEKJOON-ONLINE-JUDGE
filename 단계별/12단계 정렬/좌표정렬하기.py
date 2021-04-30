n = int(input())

num = []
for i in range(n):
    num.append(list(map(int, input().split())))

num.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    print(num[i][0], num[i][1])