while True:
    sentence = input()
    if sentence == ".":
        break
    mirror = []
    for i in sentence:
        if i in ('(', '['):
            mirror.append(i)
        elif i == ')':
            if len(mirror) != 0 and mirror[-1] == '(':
                mirror.pop()
            else:
                mirror.append(i)
        elif i == ']':
            if len(mirror) != 0 and mirror[-1] == '[':
                mirror.pop()
            else:
                mirror.append(i)
    if len(mirror) == 0:
        print('yes')
    else:
        print('no')