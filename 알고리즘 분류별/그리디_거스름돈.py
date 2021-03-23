money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

count = 0
for i in range(len(coin)):
    if money // coin[i] >= 1:
        count += money // coin[i]
        money -= (money // coin[i]) * coin[i]
    if money == 0:
        break
print(count)
