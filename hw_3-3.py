import random

rand_list = []

while len(rand_list) + 1 <=10:
    num_rand = random.randint(1, 100)
    rand_list.append(num_rand)
print(f'Список до редактирования: \n{rand_list}')

num_max = max(rand_list)
num_min = min(rand_list)
idx_max = rand_list.index(max(rand_list))
idx_min = rand_list.index(min(rand_list))
rand_list[idx_min] = num_max
rand_list[idx_max] = num_min
print(f'Список после редактирования: \n{rand_list}')
