class Account:
    def __init__(self, name):

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if (amount > self.__account_balance) and (amount > 1):
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name


