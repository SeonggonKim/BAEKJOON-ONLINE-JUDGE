import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

for i in range(n):
    while len(stack) != 0 and num_list[stack[-1]] < num_list[i]:
        answer[stack.pop()] = num_list[i]
    stack.append(i)

print(* answer)