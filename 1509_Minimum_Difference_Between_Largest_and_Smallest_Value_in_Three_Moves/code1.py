class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        length = len(nums) - 1
        nums.sort()
        
        if len(nums) > 3:
            return min(nums[length - 0] - nums[3], 
                       nums[length - 1] - nums[2], 
                       nums[length - 2] - nums[1], 
                       nums[length - 3] - nums[0])  
        else:
            return 0
