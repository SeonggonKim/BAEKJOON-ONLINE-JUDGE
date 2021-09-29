num = int(input())
answer = []

for i in range(1, num+1):
    value = str(i)
    if len(value) in (1,2):
        answer.append(i)
    else:
        diff = []
        for j in range(len(value)-1):
            diff.append(int(value[j+1]) - int(value[j]))
            diff_set = list(set(diff))
        if len(diff_set) == 1:
            answer.append(i)
print(len(answer))