class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(target):
            if target not in dp:
                if target <= 0:
                    return target == 0
                layer = 0
                for i in range(len(nums)):
                    layer += dfs(target - nums[i])
                dp[target] = layer
            return dp[target]
        return dfs(target)  