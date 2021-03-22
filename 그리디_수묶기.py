import sys

n = int(sys.stdin.readline())
number = list(int(sys.stdin.readline().strip()) for _ in range(n))

minus = [number[i] for i in range(len(number)) if number[i] <= 0]
plus = [number[i] for i in range(len(number)) if number[i] > 0]

minus.sort()
plus.sort(reverse = True)

result = []
if len(minus) % 2 == 1:
    result.append(minus[-1])
for i in range(1, len(minus), 2):
    result.append(minus[i-1] * minus[i])

if len(plus) % 2 == 1:
    result.append(plus[-1])
for i in range(1, len(plus), 2):
    if plus[i-1] != 1:
        result.append(plus[i-1] * plus[i])
    if plus[i-1] == 1:
        result.append(plus[i-1])
    if plus[i] == 1:
        result.append(plus[i])

print(sum(result))