number = list(int(input()) for _ in range(10))
answer = list(i % 42 for i in number)

new = []
count = 0
for i in answer:
    if i not in new:
        new.append(i)
        count += 1

print(count)