 '''Проведя анализ данной программы сделал вывод что память в ней расходутеся не рационально 
 в файле 6.3.1 удалось написать туже самую программу но заметно понизев задействуенную память при выполнение
  
  в 6.3.1
  избавился от списка: minus_list = []
  избавился от переменных: a, idx_max 
  
  '''

import sys
import random

rand_list = []

while len(rand_list) + 1 <=10:
    num_rand = random.randrange(-10, 10)
    rand_list.append(num_rand)
print(f'Список до редактирования: \n{rand_list}')
minus_list = []
for el in rand_list:
    if el < 0:
        minus_list.append(el)
        a = max(minus_list)
        idx_max = rand_list.index(a)
print(f'Максимальное отрицательное число: {a}\nРасположенно под индексом: {idx_max}')


sum_size = 0
sum_size += sys.getsizeof(rand_list)
sum_size += sys.getsizeof(num_rand)
sum_size += sys.getsizeof(minus_list)
sum_size += sys.getsizeof(el)
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(idx_max)
print(f' Переменные занимают: {sum_size} байт')

