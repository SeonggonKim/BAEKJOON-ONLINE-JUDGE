a = input()
b = []

for i in range(0, len(a), 10):
    b.append(a[i:i+10])

for i in b:
    print(i)