list = [input().split() for _ in range(int(input()))]

for i in range(len(list)):
    list[i][0] = int(list[i][0])

list.sort(key = lambda x: x[0])

for i in range(len(list)):
    print(list[i][0], list[i][1])