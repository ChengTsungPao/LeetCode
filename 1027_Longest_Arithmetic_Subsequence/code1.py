class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [collections.defaultdict(lambda: 1) for _ in range(n)]
        
        ans = 0
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)
                ans = max(ans, dp[i][d])
        
        return ans