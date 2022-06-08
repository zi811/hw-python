import sys
import random

rand_list = []

while len(rand_list) + 1 <=10:
    num_rand = random.randrange(-10, 10)
    rand_list.append(num_rand)
print(f'Список до редактирования: \n{rand_list}')
i = 0
while i < len(rand_list):
    if rand_list[i] >= 0:
        rand_list[i] = -11
    i+=1

print(f'Максимальное отрицательное число: {max(rand_list)}\nРасположенно под индексом: {rand_list.index(max(rand_list))}')

sum_size = 0
sum_size += sys.getsizeof(rand_list)
sum_size += sys.getsizeof(num_rand)
sum_size += sys.getsizeof(i)
print(f' Переменные занимают: {sum_size} байт')
