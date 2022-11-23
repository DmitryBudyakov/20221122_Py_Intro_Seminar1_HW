# Задача 2
# Напишите программу для проверки истинности утверждения ¬(X ˅ Y ˅ Z) = ¬X ˄ ¬Y ˄ ¬Z
# для всех значений предикат.
# ¬ - Отрицание
# ˅ - логическое "Или"
# ˄ - логическое "И"
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
expr1 = '¬(X ˅ Y ˅ Z)'
expr2 = '¬X ˄ ¬Y ˄ ¬Z'
note1 = '¬ - Отрицание'
note2 = '˅ - логическое "Или"'
note3 = '˄ - логическое "И"'

title = f'Проверка истинности утверждения {expr1} = {expr2}'
print(title)
print('где:')
print(note1)
print(note2)
print(note3)

head = f'x\ty\tz\t{expr1}\t{expr2}\tequal or not?'
print('-' * (len(head) + 24))
print(head)
print('-' * (len(head) + 24))

for x in range(2):
    for y in range(2):
        for z in range(2):
            log_expr1 = not (bool(x) or bool(y) or bool(z))
            log_expr2 = not bool(x) and not bool(y) and not bool(z)
            if log_expr1 == log_expr2:
                result = 'yes'
            else:
                result = 'not'
            
            print(f'{x}\t{y}\t{z}\t{int(log_expr1)}\t\t{int(log_expr2)}\t\t{result}')
