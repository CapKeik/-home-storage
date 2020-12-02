from account import Account


class User:
    def __init__(self, name):
        self.accounts = {'cash': set(), 'virtual': set()}

    def add_account(self, acc_type, amount = 0):
        self.accounts[acc_type].add(Account(amount))

    def get_sum_of_income(self) -> float:
        pass

    def get_sum_of_spent(self) -> float:
        pass

    def get_accounts(self) -> tuple:
        """
        returns states of all the accounts
        """
        pass

    def total_balance(self) -> float:
        pass

    def reset(self) -> None:
        """
        Deletes all information about the User
        """
        pass
