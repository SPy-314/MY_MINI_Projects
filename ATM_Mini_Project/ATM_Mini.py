class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def verify_pin(self):
        try:
            return int(input("Введите пин-код: ")) == self.pin
        except ValueError:
            print("Пин-код должен быть числом!")
            return False

    def check_balance(self):
        if self.verify_pin():
            print(f'Баланс: {self.balance} руб.')

    def withdraw(self):
        if self.verify_pin():
            try:
                amount = int(input("Введите сумму для снятия: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снято {amount} руб. Остаток: {self.balance} руб.')
                else:
                    print("Недостаточно средств!")
            except ValueError:
                print("Сумма должна быть числом!")

    def deposit(self):
        if self.verify_pin():
            try:
                amount = int(input("Введите сумму для внесения: "))
                if amount > 0:
                    self.balance += amount
                    print(f'Внесено: {amount} руб. Остаток: {self.balance} руб.')
                else:
                    print("Сумма должна быть положительной!")
            except ValueError:
                print("Сумма должна быть числом!")


def main():
    atm = ATM(1000, 1234)

    while True:
        variants = [
            "\n--- БАНКОМАТ ---",
            "1. Проверить баланс",
            "2. Снять деньги",
            "3. Внести деньги",
            "4. Выйти"
                    ]

        print(*variants, sep='\n')
        choice = input("Выберите операцию: ")
        if choice == '4':
            print("До свидания!")
            break

        operation = {
            '1': atm.check_balance,
            '2': atm.withdraw,
            '3': atm.deposit,
                    }.get(choice)

        if operation:
            operation()
        else:
            print('Неверный выбор!')


if __name__ == "__main__":
    main()