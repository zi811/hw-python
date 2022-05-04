
num = int(input('Введите трехзначное число: '))
a = num // 100
b = (num % 100) // 10
c = num % 10

sum_num = a + b + c
mult_num = a * b * c
print(f'Сумма чисел: {sum_num},\nПроизведение чисел: {mult_num}')