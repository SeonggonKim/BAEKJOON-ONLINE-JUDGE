a = []
answer = []

for _ in range(int(input())):
    a.append(input())
    answer.append([])

for i in range(len(a)):
    while True:
        if '()' in a[i]:
            a[i] = a[i].replace('()', '')
        else:
            break

for i in range(len(a)):
    if a[i] == '':
        answer[i] = 'YES'
    else:
        answer[i] = 'NO'
    print(answer[i])