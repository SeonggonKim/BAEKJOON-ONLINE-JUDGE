import sys
n = sys.stdin.readline()
list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))

list1.sort()
list2.sort(reverse=True)

def sum(x, y):
    answer = 0
    for i in range(len(x)):
        answer += x[i]*y[i]
    return answer

print(sum(list1, list2))