class Solution:
    def integerReplacement(self, n: int) -> int:
        
        memo = {}
        def recur(n):
            
            if n not in memo:
            
                if n == 1:
                    return 0

                if n % 2:
                    ans = min(recur(n - 1), recur(n + 1)) + 1
                else:
                    ans = recur(n // 2) + 1
                    
                memo[n] = ans
                
            return memo[n]
        
        return recur(n)