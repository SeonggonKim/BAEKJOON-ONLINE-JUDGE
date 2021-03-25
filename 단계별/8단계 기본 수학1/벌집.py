n = int(input())

start = 1
count = 1
six = 0

while True:
    if n > start:
        count += 1
        six += 6
        start += six
    else:
        print(count)
        break