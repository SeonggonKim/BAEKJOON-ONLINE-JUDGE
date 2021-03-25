t = int(input())
k = []
n = []
room = []

for _ in range(t):
    k.append(int(input()))
    n.append(int(input()))

for i in range(t):
    room.append([])
    for j in range(k[i]+1):
        room[i].append([])
for i in range(t):
    for j in range(1, len(room[i])):
        room[i][0] = list(range(1,n[i]+1))
        room[i][j] = list(0 for _ in range(n[i]))
        room[i][j][0] = 1

for i in range(t):
    for j in range(1, len(room[i])):
        for k in range(len(room[i][j])):
            room[i][j][k] = room[i][j][k-1] + room[i][j-1][k]

answer = [[] for _ in range(t)]
for i in range(t):
    for j in range(1, len(room[i])):
        room[i][j][0] = 1
        for k in range(len(room[i][j])):
            answer[i].append(room[i][j][k])
    print(answer[i][len(answer[i])-1])