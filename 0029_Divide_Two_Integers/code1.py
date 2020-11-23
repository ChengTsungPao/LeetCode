class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        symbol = dividend ^ divisor < 0
        if dividend == 0: 
            return 0
        elif abs(divisor) == 1:
            mid = abs(dividend)
        else:
            dividend, divisor = abs(dividend), abs(divisor)
            left, right = 0, dividend
            while left <= right:
                mid = (left + right) // 2
                temp = dividend - divisor * mid
                if temp < 0:
                    right = mid - 1
                elif temp >= divisor:
                    left = mid + 1
                else:
                    break
        val = (1 - 2 * symbol) * mid
        if -2 ** 31 <= val <= 2 ** 31 - 1:
            return val
        else:
            return 2 ** 31 - 1
