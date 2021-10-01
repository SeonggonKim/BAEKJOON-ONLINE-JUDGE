import sys
n = int(sys.stdin.readline())
list_num = []

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        list_num.append(order[1])
    elif order[0] == 'pop':
        if len(list_num) == 0:
            print(-1)
        else:
            print(list_num[-1])
            list_num.pop()
    elif order[0] == 'size':
        print(len(list_num))
    elif order[0] == 'empty':
        if len(list_num) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(list_num) == 0:
            print(-1)
        else:
            print(list_num[-1])