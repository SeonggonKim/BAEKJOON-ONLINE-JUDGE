n = int(input())
n1 = n
count = 0
while True:
    if n1 < 10:
        n1 = n1*10 + n1
        count += 1
    else:
        n1 = (n1%10)*10 + (n1//10 + n1%10) % 10
        count += 1
    if n1 == n:
        break
print(count)