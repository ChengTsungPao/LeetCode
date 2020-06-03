class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s1, s2 = 0, 0
        for n in num1:
            s1 = 10 * s1 + ord(n) - 48
        for n in num2:
            s2 = 10 * s2 + ord(n) - 48
        return str(s1 * s2)