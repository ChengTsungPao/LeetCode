class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            j = nums[i] - 1
            while not (j >= n or j < 0 or nums[i] == nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
                
        for i in range(n):
            if i != nums[i] - 1:
                return i + 1
            
        return n + 1