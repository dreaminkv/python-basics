# 4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
#Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция. Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

def num_error(number):
    if number == 13:
        raise ValueError('Value Error')
    else:
        return number**2
try:
    result = num_error(3)
except ValueError:
    print('У вас число 13 ващет')
else:
    print(result)