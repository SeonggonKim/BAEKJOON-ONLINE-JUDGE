import sys
from collections import Counter


number = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
number.sort()

print(round(sum(number)/len(number)))
print(number[len(number)//2])
mod = Counter(number).most_common()
if len(mod) >= 2 and mod[0][1] == mod[1][1]:
    print(mod[1][0])
else:
    print(mod[0][0])
print(number[-1] - number[0])

print(mod)