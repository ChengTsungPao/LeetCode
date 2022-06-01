class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(zip(nums, range(n)))
        
        suffixIndex = [0] * n
        for i in range(n - 2, -1, -1):
            suffixIndex[i] = max(suffixIndex[i + 1], nums[i + 1][1])
        
        ans = 0
        for i in range(n - 1):
            ans = max(ans, suffixIndex[i] - nums[i][1])
            
        return ans