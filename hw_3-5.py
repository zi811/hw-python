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