class Account:
    def __init__(self, balance: (int, float)):
        self.balance = balance
        self.income = 0
        self.spent = 0

    def spend(self, amount: (int, float)) -> None:
        pass

    def income(self, amount: (int, float)) -> None:
        pass

    def get_balance(self) -> (int, float):
        return self.balance

