#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for num in range(2, 10):
    result = []
    for i in range(2, 100):
        if i % num == 0:
            result.append(i)
    print(f'Для числа {num} кратны - {len(result)}. Кратные числа: {result}.')