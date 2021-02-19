class Solution:
    def fib(self, n: int) -> int:
        
        def F(n):
            if n <= 1:
                return n
            else:
                return F(n - 1) + F(n - 2)
            
        return F(n)