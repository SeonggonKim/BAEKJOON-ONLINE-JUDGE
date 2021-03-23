number = []

for i in range(9):
    number.append(int(input()))

print(max(number))

for i in range(len(number)):
    if number[i] == max(number):
        print(i+1)