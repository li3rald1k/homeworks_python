import random

secret = random.randint(1, 100)
attempts = 7

while attempts != 0:
    number = int(input('Угадай число: '))

    if number < secret:
        print('Загаданное число больше')

    elif number > secret:
        print('Загаданное число меньше')

    else:
        print('Вы победили!')
       

    attempts -= 1

if attempts == 0:
    print('Вы проиграли')
    print('Загаданное число:', secret)
