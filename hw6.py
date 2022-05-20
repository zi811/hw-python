from random import random
random_num = round(random() * 100)
i = 1
print('Давайте поиграем у,\b Вас будет 10 попыток, чтобы отгадать задуманное число, в интервале от 0 до 100')
while i <= 10:
    u_num = int(input(f'{i} поптыка, ваше число: '))
    if u_num < random_num:
        print('Написанное Вами число, меньше загаданного')
    elif u_num > random_num:
        print('Написанное Вами число, больше загаданного')
    else:
        print(f'Поздравляем! вы угадали за {i} попыток')
        break
    i += 1
print('Игра окончена')