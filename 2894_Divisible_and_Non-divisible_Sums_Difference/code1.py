class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        a1 = m
        ak = a1 + m * (k - 1)
        num2 = (a1 + ak) * k // 2
        num1 = (1 + n) * n // 2 - num2
        return num1 - num2