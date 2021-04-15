chess = list(input() for i in range(8))

hchess = []
jchess = []

for i in range(8):
    if i % 2 == 0:
        hchess.append(chess[i])
    else:
        jchess.append(chess[i])

hchess = "".join(hchess)
jchess = "".join(jchess)

hanswer = hchess[0::2]
janswer = jchess[1::2]

answer = hanswer + janswer

count = 0
for i in range(len(answer)):
    if answer[i] == 'F':
        count += 1
print(count)