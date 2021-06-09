N, X = map(int, input().split())
number = list(map(int, input().split()))

for i in number:
    if i < X:
        print(i, end = ' ')