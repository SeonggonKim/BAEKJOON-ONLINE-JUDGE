answer = []

for i in range(1, int(input())+1):
    answer.append(i)

answer.sort(reverse=True)

for i in answer:
    print(i)