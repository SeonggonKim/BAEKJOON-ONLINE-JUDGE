n = list(input())
answer = []

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        answer.append(n[i+1])

print(int((len(answer)+1)/2))