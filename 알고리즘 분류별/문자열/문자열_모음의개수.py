word = list(input())

count = 0

for i in word:
    if i in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print(count)