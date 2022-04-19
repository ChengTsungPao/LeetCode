class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        dp = [float("inf")] * (time + 1)
        
        for start, end in sorted(clips):
            for i in range(start, min(end, time) + 1):
                if start == 0:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[start] + 1)

        return dp[time] if dp[time] != float("inf") else -1