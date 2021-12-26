class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        def swap_to_end(curIndex, endIndex):
            for index in range(curIndex, endIndex - 1):
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
            return endIndex - 1
        
        index = count = 1
        endIndex = len(nums)
        
        while index < endIndex:            
            if nums[index] == nums[index - 1]:
                count += 1
            else:
                count = 1
                
            if count > 2:
                endIndex = swap_to_end(index, endIndex)
                count -= 1
            else:
                index += 1
                     
        return endIndex
