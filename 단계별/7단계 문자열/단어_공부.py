word = list(input().upper())

result = [0 for _ in range(26)]
for i in word:
    result[ord(i)-65] += 1

answer = []
for i in range(len(result)):
    if max(result) == result[i]:
        answer.append(chr(i+65))

for i in answer:
    if len(answer) == 1:
        print(i)
    else:
        print('?')
        break