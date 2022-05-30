''' Цель данного эксперемена оценить скорость выполныения 2ух алгоритмов:
С использовниям цикла while
С использовнием цикла for
на основе скорости выполнения данных алгоритмов можно сделать вывод, что разница во времени выполнения между нимим
не значительна'''


import random
import time
time_start = time.time()
rand_list = []
n = 1
count_list = []

while len(rand_list) + 1 <= 20000:
    num_rand = random.randint(1, 20000)
    rand_list.append(num_rand)

while n <= len(rand_list):
    count_list.append(rand_list.count(n))
    n += 1
print(f' Число: {count_list.index(max(count_list))+ 1} встречается: {max(count_list)} раз')

print("--- %s seconds ---" % (time.time() - time_start))


time_start = time.time()
rand_list = []
for i in range(20000):
    rand_list.append(random.randint(0,20000))

most_common = None
b = 0

for el in rand_list:
    count_num = rand_list.count(el)
    if count_num > b:
        b = count_num
        most_common = el
print(f' Чаще всего встречается число: {most_common} вот столько раз: {rand_list.count(most_common)}')

print("--- %s seconds ---" % (time.time() - time_start))