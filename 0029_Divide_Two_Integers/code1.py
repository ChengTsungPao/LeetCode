class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        symbol = dividend ^ divisor < 0
        operator = 2 ** 31 - 1
        
        A, Q, M = 0, abs(dividend), abs(divisor)
        
        for _ in range(32):
            
            A = ((A & operator) << 1) + (Q > operator)
            Q =  (Q & operator) << 1

            if A >= M:
                A -= M
                Q |= 1
                
        Q = (1 - 2 * symbol) * Q
        
        if -2 ** 31 <= Q <= 2 ** 31 - 1:
            return Q
        else:
            return 2 ** 31 - 1