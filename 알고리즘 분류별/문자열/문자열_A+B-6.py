a = list(list(list(map(int, input().split(','))) for _ in range(int(input()))))

for i in range(len(a)):
    print(a[i][0]+a[i][1])