import random

rand_list = []

while len(rand_list) + 1 <= 10:
    num_rand = random.randint(1, 10)
    rand_list.append(num_rand)
print(f'Рандомный список: {rand_list}')

min_1 = min(rand_list)
idx_min = rand_list.index(min(rand_list))
rand_list[idx_min] += 500
min_2 = min(rand_list)
print(f'Первый минимальный элемент: {min_1}\nВторой минимальный элемент: {min_2}')