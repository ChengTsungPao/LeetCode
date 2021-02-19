class Solution:
    def fib(self, n: int) -> int:
        return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5)