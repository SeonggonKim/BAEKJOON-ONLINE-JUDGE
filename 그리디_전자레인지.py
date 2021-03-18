CountA = 0
CountB = 0
CountC = 0

time = int(input())

if time // 300 >= 1:
    CountA += (time // 300)
    time -= (300*CountA)
if time // 60 >= 1:
    CountB += (time // 60)
    time -= (60*CountB)
if time // 10 >= 1:
    CountC += (time // 10)
    time -= (10*CountC)
if time != 0:
    print(-1)
else:
    print(CountA, CountB, CountC)