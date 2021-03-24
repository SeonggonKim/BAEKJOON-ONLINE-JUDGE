word = list(input())

base = list(-1 for _ in range(26))

for i in range(len(word)):
    if base[ord(word[i])-97] == -1:
        base[ord(word[i])-97] = i

for i in base:
    print(i, end = ' ')