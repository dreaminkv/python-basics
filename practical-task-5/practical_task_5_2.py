#2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает
# из него случайный элемент. Если список пустой функция должна вернуть None.
# Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
import random, sys

def number(list):
    if list == []:
        print(None)
    else:
        num = random.choice(list)
        print(num)




