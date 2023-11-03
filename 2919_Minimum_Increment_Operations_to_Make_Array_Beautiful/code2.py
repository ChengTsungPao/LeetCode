class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp1, dp2, dp3 = 0, 0, 0
        for i in range(n - 3, -1, -1):
            dp1, dp2, dp3 = min([max(k - nums[i + j], 0) + dp for j, dp in enumerate([dp1, dp2, dp3])]), dp1, dp2
        return dp1