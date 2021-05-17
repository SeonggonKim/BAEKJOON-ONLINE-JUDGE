import sys

n = int(sys.stdin.readline())
money = []
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(n):
    money.append(int(sys.stdin.readline()))

for i in money:
    answ = []
    answ.append(i // quarter)
    i%= quarter
    answ.append(i // dime)
    i%= dime
    answ.append(i // nickel)
    i%= nickel
    answ.append(i // penny)
    i%= penny
    for j in answ:
        print(j, end=' ')
    print()