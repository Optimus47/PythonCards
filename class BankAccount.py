class BankAccount:
    def __init__(self, balance):
        if balance >= 0:
            self.__balance = balance  # приватное поле
        else:
            self.__balance = 0
            # raise ValueError("Начальный баланс не может быть отрицательным")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Баланс не может быть отрицательным")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма депозита должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств или некорректная сумма")

# Пример использования
account = BankAccount(-1000)
# a ccount.balance = 2000  # Используем setter
print(account.balance)  # Вывод: 1000
account.deposit(500)
print(account.balance)  # Вывод: 1500
account.withdraw(300)
print(account.balance)  # Вывод: 1200

# account.balance = -100  # Ошибка: ValueError: Баланс не может быть отрицательным