class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = 0
        j = 0
        
        ans = float("inf")
        current_sum = 0
        
        while j < len(nums):
            current_sum += nums[j]                
                
            while current_sum >= target:
                ans = min(ans, j - i + 1)
                current_sum -= nums[i]
                i += 1
                
            j += 1
                
        return ans if ans != float("inf") else 0