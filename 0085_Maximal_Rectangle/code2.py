class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:        
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0
        dp = [[0] * n for _ in range(m)]
        
        # dynamic programming
        for i in range(m):
            for j in range(n):
                # count number of left ones 
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                    
        # monotonic stack
        for j in range(n):
            # get next smaller row (number of left ones)
            stack = []
            nextSmallerRow = [0] * m
            for i in range(m + 1):
                val = dp[i][j] if i < m else -float("inf") 
                while stack and stack[-1][0] > val:
                    preVal, preI = stack.pop()
                    nextSmallerRow[preI] = i
                stack.append((val, i))
            
            # get previous smaller row (number of left ones)
            stack = []
            prevSmallerRow = [0] * m
            for i in range(m - 1, -2, -1):
                val = dp[i][j] if i >= 0 else -float("inf") 
                while stack and stack[-1][0] > val:
                    nextVal, nextI = stack.pop()
                    prevSmallerRow[nextI] = i
                stack.append((val, i))

            # get rectangle area
            for i in range(m):
                ans = max(ans, dp[i][j] * (nextSmallerRow[i] - prevSmallerRow[i] - 1))
                            
        return ans