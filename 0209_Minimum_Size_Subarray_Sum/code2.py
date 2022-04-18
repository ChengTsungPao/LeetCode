class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans = float("inf")
        n = len(nums)
        
        s = i = j = 0
        while i < n:
            while s < target and j < n:
                s += nums[j]
                j += 1
                
            if s < target:
                break
            ans = min(ans, j - i)
            
            s -= nums[i]
            i += 1
            
        return ans if ans != float("inf") else 0