class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        symbol = dividend ^ divisor < 0
        
        A, B, Q = abs(dividend), abs(divisor), 0
        
        for i in range(31, -1, -1):
            if A >= B << i:
                A -= B << i
                Q |= 1 << i
                
        Q = -Q if symbol else Q
        
        if -2 ** 31 <= Q <= 2 ** 31 - 1:
            return Q
        else:
            return 2 ** 31 - 1