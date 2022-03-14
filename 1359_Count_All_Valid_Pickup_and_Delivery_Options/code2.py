class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(2 * n) // 2 ** n) % (10 ** 9 + 7)