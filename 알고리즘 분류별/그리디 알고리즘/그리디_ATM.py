n = int(input())
time = list(map(int,input().split()))
time.sort()
sum = 0
total = 0

for i in time:
    sum += i
    total += sum
print(total)
