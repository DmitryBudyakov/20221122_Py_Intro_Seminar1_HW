# Задача 4
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os

if os.name == 'nt':
    os.system('CLS')
else:
    os.system('clear')

title = 'Определение по номеру четверти диапазона возможных координат точки в этой плоскости.'
print('-' * len(title))
print(title)
print('-' * len(title))

quarter = int(input('Введите номер четверти координатной плоскости [1...4]: '))

if quarter == 1:
    print(f'{quarter} -> x > 0, y > 0')
elif quarter == 2:
    print(f'{quarter} -> x < 0, y > 0')
elif quarter == 3:
    print(f'{quarter} -> x < 0, y < 0')
else:
    print(f'{quarter} -> x > 0, y < 0')
    