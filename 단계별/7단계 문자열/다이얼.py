alphabet = list(input())
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sum = 0
for i in range(len(alphabet)):
    for j in dial:
        if alphabet[i] in j:
            sum += dial.index(j) + 3

print(sum)