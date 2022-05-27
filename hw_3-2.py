import random

rand_list = []
idx_list = []

while len(rand_list) + 1 <= 10:
    num_rand = random.randint(1, 10)
    rand_list.append(num_rand)
print(f'Рандомный список: {rand_list}')

for el in rand_list:
    if el % 2 == 0:
        idx_list.append(rand_list.index(el))
        rand_list[rand_list.index(el)] += 1
print(f'Индексы четных чисел: {idx_list}')