import random

a = int(input('Введите первое число диапазона: \n'))
b = int(input('Введите второе число диапазона: \n'))

print(f'Случайное число из выбранного вами диапазона = {random.randint(a, b)}')

# случайное вещественное число;

a = float(a)
b = float(b)
num = random.uniform(a, b)

print(f"Случайное вещественное число из выбранного вами диапазона = {format(num, '.3f')}")

# случайный символ.

let1 = input('Введите первую букву диапазона (английские, нижний регистр): \n')
let2 = input('Введите вторую букву диапазона (английские, нижний регистр): \n')

alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let1_ind = alph.index(let1)
let2_ind = alph.index(let2)

rand_let = alph[random.randint(let1_ind, let2_ind)]

print(f'Случайная буква из выбранного вами дипазона - "{rand_let}"')