import random

rand_list = []
n = 1

while len(rand_list) + 1 <= 100:
    num_rand = random.randint(1, 100)
    rand_list.append(num_rand)
count_list = []

while n <= len(rand_list):
    count_list.append(rand_list.count(n))
    n += 1
print(f' Число: {count_list.index(max(count_list))+ 1} встречается: {max(count_list)} раз')
