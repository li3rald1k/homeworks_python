import random

balance = 100
symbols = ["🍒", "🍋", "🔔", "7"]

print("Добро пожаловать в наебыво!")
print("У тебя", balance, "монет")

while balance > 0:
    bet = input("Ставка (или q чтобы выйти): ")

    if bet == "q":
        break

    bet = int(bet)

    if bet > balance or bet <= 0:
        print("Неправильная ставка")
        continue

    a = random.choice(symbols)
    b = random.choice(symbols)
    c = random.choice(symbols)

    print(a, b, c)

    if a == b == c:
        balance = balance + bet * 5
        print("ДЖЕКПОТ! Ты выиграл", bet * 5)
    elif a == b or b == c or a == c:
        balance = balance + bet
        print("Два одинаковых! Ты выиграл", bet)
    else:
        balance = balance - bet
        print("Проиграл")

    print("Баланс:", balance)

print("Игра окончена. Твой баланс:", balance)