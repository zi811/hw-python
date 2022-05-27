import random

rand_list = []

while len(rand_list) + 1 <= 10:
    num_rand = random.randint(1, 10)
    rand_list.append(num_rand)
print(f'Рандомный список: {rand_list}')

idx_max = rand_list.index(max(rand_list))
idx_min = rand_list.index(min(rand_list))
rand_list[idx_min] = 0
rand_list[idx_max] = 0
final_list = []

if idx_min < idx_max:
    while idx_min != idx_max:
        final_list.append(rand_list[idx_min])
        idx_min += 1
else:
    while idx_min != idx_max:
        final_list.append(rand_list[idx_max])
        idx_max += 1
print(f'Сумма чисел: {sum(final_list)}')
