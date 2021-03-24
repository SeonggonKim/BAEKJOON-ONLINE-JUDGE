n = int(input())

word = list(input() for _ in range(n))

answer =[[] for _ in range(n)]
compare = [[] for _ in range(n)]
for i in range(len(word)):
    answer[i].append(word[i][0])
    for j in range(1, len(word[i])):
        if word[i][j-1] != word[i][j]:
            answer[i].append(word[i][j])


for i in range(n):
    for j in range(len(answer[i])):
        if answer[i][j] not in compare[i]:
            compare[i].append(answer[i][j])

count = 0
for i in range(n):
    if len(compare[i]) == len(answer[i]):
        count += 1

print(count)