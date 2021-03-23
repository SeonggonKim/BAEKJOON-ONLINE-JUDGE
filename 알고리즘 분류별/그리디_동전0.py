n, money = map(int, input().split())
list = []
count = 0

for i in range(n):
    list.append(int(input()))
list.sort(reverse = True)

for i in range(n):
    if money // list[i] >= 1:
        count2 = money // list[i]
        money = money - (count2 * list[i])
        count += count2
print(count)
