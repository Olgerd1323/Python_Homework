def main():
    input_money = get_money()
    usd_money = exchange(input_money)
    print("Ты ввел ", input_money, "BYN" )
    print('Конвертированная сумма в USD = ', usd_money)

def get_money():
    input_data = input('Введите сумму для обмена: ')
    return input_data

def exchange(money):
    int_money = int(money) / 2.51
    return round(int_money, 2)
main()