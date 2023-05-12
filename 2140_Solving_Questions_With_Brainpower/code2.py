class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dp = [0] * (n + 1)
        for idx in range(n - 1, -1, -1):
            points, brainpower = questions[idx]
            if idx + brainpower + 1 < n:
                dp[idx] = max(dp[idx + 1], points + dp[idx + brainpower + 1])
            else:
                dp[idx] = max(dp[idx + 1], points)
            
        return dp[0]