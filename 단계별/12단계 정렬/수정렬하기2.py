n = int(input())

number = list(int(input()) for _ in range(n))
number.sort()

for i in number:
    print(i)