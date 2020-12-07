class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, dp = {}):
            if str(nums) not in dp:
                if nums == []:
                    return [[]]
                dp[str(nums)] = []
                for i in range(len(nums)):
                    for visited in dfs(nums[:i] + nums[i + 1:], dp):
                        dp[str(nums)] += [[nums[i]] + visited]
            return dp[str(nums)]
        return dfs(nums)