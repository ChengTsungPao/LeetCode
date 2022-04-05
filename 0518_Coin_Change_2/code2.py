class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        
        memo = {}
        def recur(amount, index):
            
            if (amount, index) not in memo:
                
                if amount == 0:
                    return 1
                elif amount < 0 or index >= len(coins):
                    return 0
                    
                memo[amount, index] = recur(amount - coins[index], index) + recur(amount, index + 1)
                
            return memo[amount, index]
        
        return recur(amount, 0)