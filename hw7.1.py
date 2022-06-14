import random, sys, time
time_start = time.time()
rand_list = []

while len(rand_list) + 1 <=100:
    num_rand = random.randrange(-100, 100)
    rand_list.append(num_rand)
print(f'Список до редактирования: \n{rand_list}')

n = 1
while n < len(rand_list):
    ls_sorted = True

    for i in range(len(rand_list) - n):

        if rand_list[i] < rand_list[i + 1]:
            rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
            ls_sorted = False

    if ls_sorted == True:
        break

    n += 1

print(f'\nСортировка методом пузыря:\n{rand_list}')

sum_size = 0
sum_size += sys.getsizeof(rand_list)
sum_size += sys.getsizeof(n)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(ls_sorted)

print(f'Переменные занимают: {sum_size} байт')
print(f'\nВремя выполнения: \n{(time.time() - time_start)} секунд')
