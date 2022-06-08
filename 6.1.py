'''Размер этой программы зависит от количества четных чисел в списке rand_list, чем больше четных
чисел в списке, тем больш чисел добавится в idx_lixt '''

import sys
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

sum_size = 0
sum_size += sys.getsizeof(rand_list)
sum_size += sys.getsizeof(idx_list)
sum_size += sys.getsizeof(num_rand)
sum_size += sys.getsizeof(el)
print(f' Переменные занимают: {sum_size} байта')



import sys
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

sum_size = 0
sum_size += sys.getsizeof(rand_list)
sum_size += sys.getsizeof(idx_list)
sum_size += sys.getsizeof(num_rand)
sum_size += sys.getsizeof(el)
print(f' Переменные занимают: {sum_size} байта')

