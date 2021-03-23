n = int(input())
rope = []
a = []

for i in range(n):
    rope.append(int(input()))
rope.sort()

for i in range(n):
    a.append(rope[i]*(n-i))

print(max(a))
