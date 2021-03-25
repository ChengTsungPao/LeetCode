class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def recur(i, j, memo = {}):
            if (i, j) not in memo:
                
                if i == j:
                    return 0
                
                memo[i, j] = max(piles[i] - recur(i + 1, j, memo), piles[j] - recur(i, j - 1, memo))
                
            return memo[i, j]
        
           
        return recur(0, len(piles) - 1, {}) > 0