#1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

#   Примечание: Списки фруктов создайте вручную в начале файла.
res = []
fruits_one = ['Ананас', 'Дракон', 'Банан', 'Киви', 'Мандарин']
fruits_two = ['Ананас', 'Лимон', 'Дракон', 'Мандарин']

fruits_one_two = [fruit for fruit in fruits_one if fruit in fruits_two]
print(fruits_one_two)