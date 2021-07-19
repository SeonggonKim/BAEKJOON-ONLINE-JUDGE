word = list(input())

if word.count('U')<1 or word.count('C')<2 or word.count('P')<1:
    print('I hate UCPC')

else:
    if 'U' in word:
        word = word[word.index('U')+1:]

    if 'C' in word:
        word = word[word.index('C')+1:]

    if 'P' in word:
        word = word[word.index('P')+1:]

    if 'C' in word:
        print('I love UCPC')
    else:
        print('I hate UCPC')