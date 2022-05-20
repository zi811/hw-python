num =(list(input('Введите число: ')))
i = 0
even = 0
uneven = 0
while i < len(num):
    if (int(num[i]) % 2) == 0:
        even += 1
    else:
        uneven += 1
    i += 1
print(f'Четных чисел: {even} \nНечетных чисел: {uneven}')