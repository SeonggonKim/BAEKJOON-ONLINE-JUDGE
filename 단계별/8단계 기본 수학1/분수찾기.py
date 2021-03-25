n = int(input())

max = 0
jum = 1

while True:
    if n > max:
        max += jum
        jum += 1
    else:
        result = jum-1
        break

answer = [[] for _ in range(result)]

if result % 2 == 0:
    for i in range(1, result+1):
        answer[i-1].append(i)
        answer[i-1].append(result+1-i)
else:
    for i in range(1, result+1):
        answer[i-1].append(result+1-i)
        answer[i-1].append(i)

print(answer[len(answer)-(max-n)-1][0],answer[len(answer)-(max-n)-1][1], sep='/')