n = int(input())
i = 0
for _ in range(n):
    i += 1
    A, B = map(int, input().split())
    print("Case #" + str(i) + ": " + str(A+B), sep = " ")