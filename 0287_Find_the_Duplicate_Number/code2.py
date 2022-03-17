class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        while True :         
            index = nums[0]
            if nums[index] == "#":
                return nums[0]
            else:
                nums[0], nums[index] = nums[index], nums[0]
                nums[index] = "#"
            
        return 0