class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        i = j = 1        
        count = 1
        num = nums[0]
        
        while j < n:
            if nums[j] == num:
                count += 1
            else:
                count = 1
                
            if count > 2:
                j += 1
                continue
                
            num = nums[j]
            nums[i] = nums[j]
            i += 1
            j += 1

        return i