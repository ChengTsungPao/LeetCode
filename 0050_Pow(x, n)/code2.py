class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # 2**14 = 2**8 x 2**4 x 2**2 (14 = 0b1110) 
        
        def pow2(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            
            ans = x
            count = 1
            while count * 2 <= n:
                ans *= ans
                count *= 2
                
            return ans
        

        ans = 1
        digitVal = 1
        
        n_ = abs(n)
        while n_ > 0:
            if n_ % 2 == 1:
                ans *= pow2(x, digitVal)
            n_ //= 2
            digitVal *= 2
        
        return  ans if n >= 0 else 1 / ans