class Account:
    def __init__(self, name):

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> float:
        '''
        Deposits Money into account
        :param amount: Amount being deposited
        :return: returns boolean
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> float:
        '''
        Withdraws money from account
        :param amount: amount being withdrawn
        :return: True if money withdrawn, false if not
        '''
        if (amount < self.__account_balance) and (amount > 0):
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Gets the account balance
        :return: Returns the account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Gets the account name
        :return: Returns the account name
        '''
        return self.__account_name


