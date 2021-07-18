word = input()
find = input()

if find in word:
    answer = word.replace(find,'')
    count = int((len(word) - len(answer)) / len(find))
else:
    count = 0

print(count)