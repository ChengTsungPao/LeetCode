class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        
        dp = [[[] for j in range(target + 1)] for i in range(n)]
        for i in range(n):
            dp[i][0] = [[]]
            
        for i in range(n - 1, -1, -1):
            for j in range(1, target + 1):
                for k in range(i, n):
                    if j - candidates[k] >= 0:
                        for ret in dp[k][j - candidates[k]]:
                            dp[i][j].append([candidates[k]] + ret)
                            
        return dp[0][target]