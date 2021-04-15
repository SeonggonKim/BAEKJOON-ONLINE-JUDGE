a = list(input())

alphabet = [0 for _ in range(26)]

for i in a:
    alphabet[ord(i)-97] += 1

for i in range(26):
    print(alphabet[i], end=' ')