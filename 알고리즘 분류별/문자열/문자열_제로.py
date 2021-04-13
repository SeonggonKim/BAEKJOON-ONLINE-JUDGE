n = int(input())
number = []

for _ in range(n):
    number.append(int(input()))
    if number[-1] == 0:
        number.pop()
        number.pop()

print(sum(number))