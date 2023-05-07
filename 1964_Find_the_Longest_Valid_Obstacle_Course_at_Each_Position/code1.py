class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if obstacles[i] >= obstacles[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp