import sys

n, m = map(int, sys.stdin.readline().split())

nohear = {sys.stdin.readline().strip() for i in range(n)}
nolook = {sys.stdin.readline().strip() for i in range(m)}

nohearlook = list(nohear & nolook)
nohearlook.sort()
print(len(nohearlook))
for i in nohearlook:
    print(i)