import sys

word = sys.stdin.readline().strip()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
answer = []

for i in alphabet:
    if i in word:
        word = word.replace(i,"!")
print(len(word))