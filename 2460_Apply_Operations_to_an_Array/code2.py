class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        j = 0
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            if nums[i] > 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
        return nums