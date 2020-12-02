from account import Account


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = set()
        self.categories = {'food': 0,
                           'housing': 0,
                           'health': 0,
                           'car': 0,
                           'clothes': 0,
                           'pets': 0,
                           'gifts': 0,
                           'connection': 0}

    def add_account(self, name, balance=0):
        self.accounts.add(Account(balance, name))

    def get_total_income(self) -> float:
        total_income = 0
        for account in self.accounts:
            total_income += account.income
        return total_income

    def get_sum_of_spent(self) -> float:
        total_spent = 0
        for account in self.accounts:
            total_spent += account.spent
        return total_spent

    def get_total_balance(self) -> float:
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return total_balance

    def reset(self) -> None:
        """
        Deletes all information about the User
        """
        pass
