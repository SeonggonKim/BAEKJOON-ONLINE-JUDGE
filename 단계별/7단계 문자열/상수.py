import sys

A, B = sys.stdin.readline().split()

a = list(A)
b = list(B)

sum1 = 0
for i in range(len(a)):
    sum1 += (int(a[i]) * 10**(i))

sum2 = 0
for i in range(len(b)):
    sum2 += (int(b[i]) * 10**(i))

print(max(sum1,sum2))