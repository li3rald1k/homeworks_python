
while 1:
    try:
        symbols = ['+', '-', '*', '/']
        number_1 = float(input('введите первое число: '))
        operation = str(input('укажите операцию: + - * / '))
        if operation not in symbols:
            raise ValueError('Неверная операция')
        number_2 = float(input('введите второе число: '))
        
        if operation == '+':
            print(f'{number_1}+{number_2}={number_1+number_2}')
        elif operation == '-':
            print(f'{number_1}-{number_2}={number_1-number_2}')
        elif operation == '*':
            print(f'{number_1}*{number_2}={number_1*number_2}')
        elif operation == "/":
            if number_2 == 0:
                print('Ошибка деления на 0')
            else:
                print(f'{number_1}/{number_2}={number_1/number_2}')
        print('-'*40)
    except ValueError:
        print('проверьте корректность ввода данных')
        print('-'*40)
        continue

