class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = collections.defaultdict(int)
        
        for w in range(1, len(piles)):
            
            for s in range(0, len(piles) - w):
                
                i, j = s, s + w  
                
                dp[i, j] = max(piles[i] - dp[i + 1, j], piles[j] - dp[i, j - 1])
           
        return dp[0, len(piles) - 1] > 0