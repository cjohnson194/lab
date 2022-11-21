class Account:
    '''
    A class representing details of an account
    '''
    def __init__(self, name: str, balance=0) -> None:
        '''
        Constructor to set name for account name and balance to 0
        :param name: name of account
        '''

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Deposits Money into account
        :param amount: Amount being deposited
        :return: returns boolean True if money was deposited, false if not
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
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


