class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index):
            if index not in dp:
                if index == len(nums):
                    return 0
                s = 1
                for i in range(index + 1, len(nums)):
                    if nums[index] < nums[i]:
                        s = max(s, dfs(i) + 1)
                dp[index] = s
            return dp[index]
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans