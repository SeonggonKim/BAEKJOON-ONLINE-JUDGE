a = int(input())
h = []

for i in range(a):
    h.append(list(map(int, input().split())))

h.sort(key = lambda i: (i[1], i[0]))

count = 0
end_time = 0
for i in range(a):
    if h[i][0] >= end_time:
        count += 1
        end_time = h[i][1]

print(count)