class Solution:
    def intToRoman(self, num: int) -> str:
        
        table = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        
        ans = ""
        base = 1
        while num > 0:
            n = num % 10
            if n == 9:
                ans = table[1 * base] + table[10 * base] + ans
            elif n >= 5:
                ans = table[5 * base] + (n - 5) * table[1 * base] + ans
            elif n == 4:
                ans = table[1 * base] + table[5 * base] + ans
            elif n > 0:
                ans = n * table[1 * base] + ans
            num //= 10
            base *= 10

        return ans