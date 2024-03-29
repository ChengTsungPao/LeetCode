class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        
        memo = {}
        def recur(amount, index):
            
            if (amount, index) not in memo:

                if amount == 0:
                    return 1
                elif amount < 0:
                    return 0
                
                count = 0
                for i in range(index, len(coins)):
                    count += recur(amount - coins[i], i)
                    
                memo[amount, index] = count
                
            return memo[amount, index]
        
        return recur(amount, 0)