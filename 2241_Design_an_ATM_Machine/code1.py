class ATM:

    def __init__(self):
        self.count = [0] * 5
        self.money = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, c in enumerate(banknotesCount):
            self.count[i] += c

    def withdraw(self, amount: int) -> List[int]:
        costCount = [0] * 5
        for i in range(len(self.count) - 1, -1, -1):
            if self.count[i] > 0:
                c = amount // self.money[i]
                costCount[i] = c if c <= self.count[i] else self.count[i]
                amount -= self.money[i] * costCount[i]
        if amount == 0:
            for i, c in enumerate(costCount):
                self.count[i] -= c
            return costCount
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)