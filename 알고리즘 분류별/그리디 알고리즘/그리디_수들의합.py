n = int(input())

sum = 0
plus = 1
count = 0

while sum <= n:
    sum += plus
    plus += 1
    count += 1

print(count-1)