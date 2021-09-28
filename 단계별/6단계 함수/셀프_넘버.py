num_all = list(i for i in range(1, 10001))

not_generator = []

for i in num_all:
    value = str(i)
    value_sum = int(value)
    for j in range(len(value)):
        value_sum += int(value[j])
    not_generator.append(value_sum)

for i in num_all:
    if i not in not_generator:
        print(i)
        