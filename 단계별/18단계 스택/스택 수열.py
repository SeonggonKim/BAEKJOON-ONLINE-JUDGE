import sys

n = int(sys.stdin.readline())
stack = []
answer = []
cnt = 0

for i in range(n):
    num = int(sys.stdin.readline())
    while num > cnt:
        cnt += 1
        stack.append(cnt)
        answer.append("+")
    if stack[-1] == num:
        stack.pop()
        answer.append('-')

if len(stack) != 0:
    print('NO')
else:
    for i in answer:
        print(i)