
print("Hello Python from Visual Studio")
s = "*"*30
print(s)
print("New project")

#Простейшая арифметика задание 5 (дома)
import math

days = int(input('Введите количество дней: '))

percent = float(input('Введите процент скидки (например 10;15.5): '))
percent = 1 - (percent / 100)

first_sum = float(input('Сумма в долларах: '))
print()
final_sum = (first_sum + 3 * days) * percent
print( 'Итоговая сумма: {0}$'.format(final_sum) )
input()