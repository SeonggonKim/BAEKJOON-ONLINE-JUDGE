a = input().split('-')
plus = []
minus = []

for i in range(len(a)):
    if i == 0:
        plus.append(a[i].split('+'))
    else:
        minus.append(a[i].split('+'))

realplus = []
for i in range(len(plus)):
    for j in range(len(plus[i])):
        realplus.append(int(plus[i][j]))

realminus = []
for i in range(len(minus)):
    for j in range(len(minus[i])):
        realminus.append(int(minus[i][j]))

sum = 0
for i in realplus:
    sum += i

for i in realminus:
    sum -= i
print(sum)
