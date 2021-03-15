import math
N = int(input())
a = math.trunc(N/5)
count = 0

if N % 5 == 0:
    count = N // 5
elif N % 5 != 0:
    for i in range(a+1):
        if (N-5*i) % 3 != 0:
            count = -1
    for i in range(a + 1):
        if (N-5*i) % 3 == 0:
            count = ((N-5*i) // 3) + i
print(count)