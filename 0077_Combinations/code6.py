class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        dp = [[[[]]] + [[] for _ in range(k)] for _ in range(n + 2)]
        
        for i in range(n, 0, -1):
            for j in range(1, k + 1):
                dp[i][j] = copy.deepcopy(dp[i + 1][j]) 
                for ret in dp[i + 1][j - 1]:
                    dp[i][j].append([i] + ret)
                    
        return dp[1][k]