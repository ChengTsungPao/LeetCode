class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        def recur(left, right, memo = {}):
            
            if (left, right) not in memo:
            
                if left >= right:
                    return 0

                ans = float("inf")
                for guess in range(left, right + 1):
                    ans = min(ans, max(recur(left, guess - 1), recur(guess + 1, right)) + guess)
                    
                memo[left, right] = ans
                
            return memo[left, right]
        
        return recur(1, n)
        