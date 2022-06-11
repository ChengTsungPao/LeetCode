class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = -float("inf")
        value, totalSum = 0, sum(nums)
        for i in range(n):
            value += nums[i] * i
        ans = max(ans, value)
        
        for i in range(n):
            value = value - (totalSum - nums[i]) + (n - 1) * nums[i]
            ans = max(ans, value)
        
        return ans