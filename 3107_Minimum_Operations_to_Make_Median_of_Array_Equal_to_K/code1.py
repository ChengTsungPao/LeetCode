class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        ans = abs(nums[n // 2] - k)
        for i, num in enumerate(nums):
            if i < n // 2:
                ans += max(num - k, 0)
            elif i > n // 2:
                ans += max(k - num, 0)
                
        return ans    