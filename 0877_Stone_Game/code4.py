class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        '''
        Recursion
            i => 0 ~ n
            j => n - 1 ~ -1
        '''
        
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n, -1, -1):
            for j in range(-1, n, 1):
                if i > j:
                    j += 1 # shift
                    dp[i][j] = 0
                else:
                    j += 1 # shift
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j - 1] - dp[i][j - 1])
                    
        return dp[0][n] >= 0