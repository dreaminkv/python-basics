# Игра "Угадай число"
import random

#Шаг 1 ввод необходимых переменных
number = random.randint(1, 100) # Создание рандомного числа для игры, которое должны угадать игроки
print(number) # Элемент можно спрятать, что бы не знать подсказку
number_user = None # Объявим в программу переменную, которая будет отвечать за введенную тем или иным игроком цыфры, пока
# она будет содержать в себе ничего
count = 0 # попытки
levels = {1: 10, 2: 5, 3: 3} # Добавим в программу возможность выбора сложности, это словарь с возможностью выбрать уровень сложности
max_count = levels[int(input('Введите сложность игры 1-3: '))]
user_count = int(input('Введите количество игроков: '))
users = [] # Сделаем пустой список, в дальнейшем мы в него занесем имена игроков

for i in range(user_count): # Создадим цикл, благодаря которуму сможем определить количество игроков и дать им имена
    user = input(f'Введите имя игрока №{i+1}: ') # Создадим перемнную user, что бы в дальнейшем занести имена в users
    users.append(user) # Добавим игрока в список users
print(f'Имена играков учавствующих в игре: {users}')

while number_user != number: # Создадим бесконечный цикл while, в которым главным условием продолжения цикла это не равенство
                             # задуманного числа и объявленного игроком, если кажется, что можно поставить условие True
                             # то это не так, учавствуют несколько игроков, если даже один из них угадает и break прервет
                             # цикл, то проверку бесконечного цикла это не остановит и он будет продолжать опрашивать других играков,
                             # а так он просто закроется по условию
    count += 1 # счетчик попыток, для возможности регулировать сложность
    if count > max_count: # Условия при котором игра заканчивается, так как игроки не уложились в количество попыток
        print('Все проиграли')
        break
    print(f'Попытка № {count}') # Обозначим номер попытки
    for player in users: # цикл для перебора игроков
        number_user = int(input(f'Игрок {player} Вводит число: ')) # Игрок из списка users вводит свое число, что бы угадать
        if number_user == number: # Если игрок угадал, то это условие завершает программу
            print(f'Победил игрок {player}')
            break
        elif number_user > number: # если число больше чем загаданное, то программа напечатате тэто соббщение и пойдет по новому циклу
            print('Число больше чем загаданное')
        elif number_user < number:
            print('Число меньше чем загаданное')# если число меньше чем загаданное, то программа напечатате тэто соббщение и пойдет по новому циклу
