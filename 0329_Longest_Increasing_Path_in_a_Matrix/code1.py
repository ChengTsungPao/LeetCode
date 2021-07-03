class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j, preNum = -float("inf"), memo = {}):
            
            if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
                return 0

            if matrix[i][j] <= preNum:
                return 0
            
            if (i, j) not in memo:
                memo[i, j] = max(dfs(i + 1, j, matrix[i][j]), 
                                 dfs(i - 1, j, matrix[i][j]), 
                                 dfs(i, j + 1, matrix[i][j]), 
                                 dfs(i, j - 1, matrix[i][j])) + 1
            return memo[i, j]
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))

        return ans     
