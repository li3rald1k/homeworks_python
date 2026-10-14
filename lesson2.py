# # Условные операторы и циклы


# import random

# while room <= 10:
#     print()
#     print('Ты вошел в комнату', room)

#     event = random.randint(1, 3)

#     if event == 1:
#         print('На тебя напал монстр 😈')
#         print('Ты убежал 😃')

#     elif event == 2:
#         print('Ты нашел 10 монет')
#         coins += 10

#     else:
#         print('🙂 Комната пустая!')

#     room += 1

# print()
# print('🧭 Ты прошел все комнаты')
# print(f"👑 ты собрал монет - {coins}")




# Циклы  for, while
# for - от точки а до точки б и завершается
# while - бесконечный (пока значение не станет ложным!)

# source = 10

# while source != 0:
#     color = str(input('какой свет горит? '))
#     color = color.lower()
#     print(f'кол-во ресурсов - {source}')
#     source -= 1
#     print(f'Остаток ресурсов - {source}')

#     if color == 'зеленый':
#         print('Можете ехать!')

#     elif color == 'желтый':
#         print('Приготовьтесь к движению')

#     elif color == 'красный':
#         print('Стоп!')

#     else:
#         print('Смотрите на знаки!')
#         continue

#     if source == 0:
#         print('Кончились ресурсы требуется кап ремонт!')
#         break





# = - присвоение, == - сравнение или приравнение

# >=, <=, !=, ==, or, and

# с 21 января по 19 февраля.
# day = int(input('Введите день вашего рождения! '))
# month = int(input('Введите месяц вашего! '))

# if day>=21 and day<=31 and month == 1 or day<=19 and day>=1 and month==2:
#     print('Вы Водолей!')
# else:
#     print('Вы не водолей')






# color = str(input('какой свет горит? '))
# color = color.lower()

# if color == 'зеленый':
#     print('Можете ехать!')

# elif color == 'желтый':
#     print('Приготовьтесь к движению')

# elif color == 'красный':
#     print('Стоп!')

# else:
#     print('Смотрите на знаки!')
money = 1000
start_money = money

while money != 0:
    print('2 — Купить молоко')
    print('3 — Купить шоколад')
    print('4 — Показать остаток денег')
    print('0 — Выйти')

    cash = int(input('Выберите действие: '))

    if cash == 1:
        if money >= 50:
            money -= 50
            print('Хлеб куплен')
        else:
            print('Недостаточно денег')

    elif cash == 2:
        if money >= 80:
            money -= 80
            print('Молоко куплено')
        else:
            print('Недостаточно денег')

    elif cash == 3:
        if money >= 150:
            money -= 150
            print('Шоколад куплен')
        else:
            print('Недостаточно денег')

    elif cash == 4:
        print('Осталось денег -', money)

    elif cash == 0:
       break

    else:
        print('Неверный выбор')

print('Вы потратили:', start_money - money)
print('Осталось:', money)

# login = "admin"
# password = "12345"
# attempts = 3

# while attempts != 0:
#     user_login = input('Введите логин: ')
#     user_password = input('Введите пароль: ')

#     if user_login == login and user_password == password:
#         print('Добро пожаловать!')
        

#     else:
#         attempts -= 1
#         print('Неверный логин или пароль')
#         print('Осталось попыток:', attempts)

#     if attempts == 0:
#         print('Аккаунт заблокирован')
# import random

# secret = random.randint(1, 50)
# attempts = 7

# while attempts != 0:
#     number = int(input('Угадай число: '))

#     if number < secret:
#         print('Загаданное число больше')

#     elif number > secret:
#         print('Загаданное число меньше')

#     else:
#         print('Вы победили!')
       

#     attempts -= 1

# if attempts == 0:
#     print('Вы проиграли')
#     print('Загаданное число:', secret)

