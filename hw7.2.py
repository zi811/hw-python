import random
import sys
import time

time_start = time.time()


def merge_sort(rand_list):
    if len(rand_list) <= 1:
        return rand_list

    left = merge_sort(rand_list[:len(rand_list) // 2])
    right = merge_sort(rand_list[len(rand_list) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            rand_list[i + j] = left[i]
            i += 1
        else:
            rand_list[i + j] = right[j]
            j += 1

    while len(left) > i:
        rand_list[i + j] = left[i]
        i += 1
    while len(right) > j:
        rand_list[i + j] = right[j]
        j += 1

    return rand_list


rand_list = []

while len(rand_list) + 1 <= 100:
    num_rand = round(random.uniform(1, 50), 2)
    rand_list.append(num_rand)
print(f'Список до редактирования: \n{rand_list}')

merge_sort(rand_list)
print(f'\nПосле сортировки методом слияния:\n{rand_list}')

sum_size = 0
sum_size += sys.getsizeof(rand_list)

print(f'\nПеременные занимают: {sum_size} байт')
print(f'\nВремя выполнения: \n{(time.time() - time_start)} секунд')
