n = int(input())

list = list(list(map(int, input().split())) for _ in range(n))

list.sort(key = lambda x: (x[1], x[0]))

for i in range(n):
    print(list[i][0], list[i][1])