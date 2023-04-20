class Account:
    """
    A class representing a bank account.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize a new account with a name and balance of 0.
        :param name: Account holder name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Add the specified amount to the account balance.
        :param amount: Amount added to balance
        :return: True if the deposit was successful, False otherwise.
        """
        if amount <= 0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float -> bool):
        """
        Subtract the specified amount from the account balance.
        :param amount: Amount subtracted from balance
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        """
        Method to get the balance associated with this account.
        :return: Current Balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get the name associated with this account.
        :return: Account holders name
        """
        return self.__account_name
