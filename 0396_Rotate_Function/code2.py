class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = -float("inf")
        windowSum = value = 0
        for i in range(n):
            value += nums[i] * i
            windowSum += nums[i]
        ans = max(ans, value)
        
        for i in range(n, 2 * n):   
            value = value - (windowSum - nums[i - n]) + (n - 1) * nums[i % n]
            windowSum = windowSum - nums[i - n] + nums[i % n]
            ans = max(ans, value)
        
        return ans