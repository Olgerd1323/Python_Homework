

def main():
    input_money = get_money()
    usd_money = exchange_usd(input_money)
    eur_money = exchange_eur(input_money)
    chf_money = exchange_chf(input_money)
    gbp_money = exchange_gbp(input_money)
    cny_money = exchange_cny(input_money)
    print("Ты ввел ", input_money, "BYN")
    print('Конвертированная сумма в USD = ', usd_money)
    print('Конвертированная сумма в EUR = ', eur_money)
    print('Конвертированная сумма в CHF = ', chf_money)
    print('Конвертированная сумма в GBP = ', gbp_money)
    print('Конвертированная сумма в CNY = ', cny_money)


def get_money():
    input_data = int(input('Введите сумму для обмена BYN: '))
    if input_data < 0:
        print('Введите положительное число')
        while True:
            input_data = input('Введите сумму для обмена BYN: ').strip()
            if input_data.isdigit():
                input_data = int(input_data)
                break
            else:
                if not input_data:
                    print('Вы ввели пустое поле. Введите число')
                else:
                    print('Вы ввели не число. Введите число')
    return input_data


def exchange_usd(money):
    int_money = int(money) / 2.5
    return round(int_money, 2)


def exchange_eur(money):
    int_money = int(money) / 2.95
    return round(int_money, 2)


def exchange_chf(money):
    int_money = int(money) / 2.71
    return round(int_money, 2)


def exchange_gbp(money):
    int_money = int(money) / 3.46
    return round(int_money, 2)


def exchange_cny(money):
    int_money = int(money) / 3.88
    return round(int_money, 2)


main()