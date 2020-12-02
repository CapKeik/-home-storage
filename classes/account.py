class Account:
    def __init__(self, balance: (int, float), name: str):
        self.balance = balance
        self.income = 0
        self.spent = 0
        self.name = name

    def spend(self, amount: (int, float)) -> None:
        self.balance -= amount
        self.spent += amount

    def income(self, amount: (int, float)) -> None:
        self.balance += amount
        self.income += amount

    def get_balance(self) -> (int, float):
        return self.balance
