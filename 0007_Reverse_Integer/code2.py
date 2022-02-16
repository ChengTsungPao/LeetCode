class Solution:
    def reverse(self, x: int) -> int:
        
        symbol = abs(x) // x if x != 0 else 1
        x = abs(x)
        
        ans = 0
        while x > 0:
            ans = 10 * ans + x % 10
            x //= 10
        ans *= symbol
            
        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0