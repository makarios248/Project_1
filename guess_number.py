# Угадайка чисел
# Описание проекта: программа генерирует случайное число в диапазоне
# от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести
# сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна поздравить
# его и вывести сообщение 'Вы угадали, поздравляем!'.

# 1. Добавьте подсчет попыток, сделанных пользователем.
# Когда число отгадано, программа должна показать количество попыток;
# 2. Добавьте возможность генерации нового числа (повторная игра),
# после того, как пользователь угадал число;
# 3. Добавить возможность указания левой и правой границы для
# случайного выбора числа (от n до n).


import random


def play_range():  # устанавливаем диапазон для загадывания числа
    print('Укажите 2 числа, в каком диапазоне хотите угадывать')
    while True:
        start_num, stop_num = input(), input()
        if start_num.isdigit() and stop_num.isdigit():
            if stop_num < start_num:
                start_num, stop_num = stop_num, start_num
            return int(start_num), int(stop_num)
        else:
            print('Введите 2 числа:')


def is_valid_input(start=1, stop=100):  # проверка ввода числа
    start, stop = play_range  # не могу разобраться, как передать
    # в эту функцию, два числа из функции play_range()
    while True:
        user_number = input(f'Введите число от {start} до {stop}: ')
        if user_number.isdigit() and 0 < int(user_number) < 100:
            return int(user_number)
        else:
            print(f'А может быть все-таки введем целое число от'
                  f' {start} до {stop}?')


def is_guess_num(start=1, stop=100):  # угадываем число
    start, stop = play_range  # не могу разобраться, как передать
    # в эту функцию, два числа из функции play_range()
    guess_number = random.randint(start, stop)
    counter = 1
    while True:
        number = is_valid_input()
        if number < guess_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif number > guess_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        elif number == guess_number:
            print(f'Вы угадали, поздравляем! Количество попыток: {counter}')
            start_new_game()


def start_new_game():  # хотите ли сыграть еще раз?
    while True:
        play_again = input('Сыграем еще раз? (д/н) ').lower()
        if play_again != 'д' and play_again != 'н':
            print('Введите "д", чтобы продолжить, и "н", чтобы завершить игру')
        elif play_again == 'д':
            is_guess_num()
        elif play_again == 'н':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


def guess_game():  # запуск игры
    print('Добро пожаловать в числовую угадайку')
    while True:
        answer = input('Хотите выбрать диапазон, в котором будет '
                       'загадано число? (д/н) ').lower()
        if answer != 'д' and answer != 'н':
            print('Введите "д", чтобы выбрать, и "н", чтобы начать игру')
        elif answer == 'д':
            play_range()
            break
    is_guess_num()


guess_game()  # вызов игры
