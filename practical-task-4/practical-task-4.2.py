#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def big_three(one_num, two_num, three_num):
    result = sorted((one_num, two_num, three_num), reverse=True)
    return result[0]

print(big_three(1, 2, 5))

def big_num(a, b, c):
    result = max(a, b, c)
    return result
print(big_num(2, 3, 11))