class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = collections.defaultdict(int)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
            ans = max(ans, dp[i])
        return ans