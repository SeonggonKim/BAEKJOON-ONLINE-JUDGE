n = int(input())
word = []

for i in range(n):
    word.append(list(input()))

word.sort(key = lambda x: len(x), reverse = True)
print(word)
dic = {}
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]] = 10 ** (len(word[i])-j-1)
        else:
            dic[word[i][j]] += 10 ** (len(word[i])-j-1)

dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
print(dic)

answer = []
number = 9
for i in range(len(dic)):
    answer.append(dic[i][1] * number)
    number -= 1
print(answer)

print(sum(answer))

# N = int(input())
#
# a = list(map(lambda x:ord(x) - ord('A'),(input())) for _ in range(N))
#
# k = []
# for i in a:
#     b = []
#     for j in i:
#         b.append(j)
#     k.append(b)
#
# check = [0]*(ord('Z')-ord('A')+1)
#
#
# for i in range(N):
#     count = 0
#     for j in k[i][::-1]:
#         check[j] += 10**count
#         count += 1
#
#
# check.sort(reverse=True)
#
# answer = 0
# num = 9
# for i in range(len(check)):
#     if check[i] == 0:
#         break
#     answer += num*check[i]
#     num -= 1
# print(answer)
