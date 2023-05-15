class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        if k == 0:
            return nums[0] if len(nums) > 0 else -1
        elif k == 1:
            return nums[1] if len(nums) > 1 else -1
        elif n == 1 and k % 2 == 1:
            return -1
            
        j = maxVal = 0
        for i in range(min(k - 1, n)):
            maxVal = max(maxVal, nums[i])
            j += 1
        
        if n - j <= 1:
            return maxVal
        
        return max(maxVal, nums[j + 1])