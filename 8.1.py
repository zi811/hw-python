s = str(input('Введите строку: ').lower())

print(f'Строка {s} имеет длину {len(s)} сиволов.')

subset = set()
for i in range(len(s)):
    for j in range(len(s) - 1
                   if i == 0
                   else len(s), i, -1):
        subset.add(hash(s[i:j]))

print(f'Количество различных подстрок в этой строке: {len(subset)}')
