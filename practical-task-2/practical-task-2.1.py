#1: Даны два произвольные списка. Удалите из первого списка
# элементы присутствующие во втором списке.
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3, 4]
for number in my_list_1[:]:   # Здесь в цикле необходим срез, что бы цикл прошел по всему диапазону my_list_1,
    # иначе из за удаления чисел, диапазон будет смещаться и не все числа будут проверены
    if number in my_list_2:
        my_list_1.remove(number)

print(my_list_1)