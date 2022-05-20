n = int(input())
n_list = []

while n > 0:
    n_list.append(n)
    n -= 1
nn = int(n_list[0]*(n_list[0] + 1)/2)
print(f'Сумма чисел = \n{sum(n_list)}\n Число по формуле: n(n-1)/2 = \n{nn}')