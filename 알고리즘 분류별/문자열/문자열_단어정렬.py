n = int(input())

word = list(input() for _ in range(n))
word_list = list(set(word))

word_list_sort = sorted(word_list, key=lambda x: (len(x),x), reverse = False)

for i in word_list_sort:
    print(i)