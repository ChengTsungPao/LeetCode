class Solution:
    def integerBreak(self, n: int) -> int:
        
        # 根據算幾不等式，當數字總和固定時，數字越靠近乘積會越大
        
        def calculate(n, cut):
            x = n // cut
            r = n % cut
            return (x ** (cut - r)) * (x + 1) ** r
            
        ans = 0
        for cut in range(2, n + 1):
            ans = max(ans, calculate(n, cut))
        
        return ans