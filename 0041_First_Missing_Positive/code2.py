# Time: O(N)
# Space: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        index = 0
        while index < len(nums):
            i, j = index, nums[index] - 1
            if nums[index] - 1 == index or nums[index] <= 0 or nums[index] >= len(nums) + 1 or nums[i] == nums[j]:
                index += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        ans = len(nums) + 1    
        for index in range(len(nums)):
            if nums[index] - 1 != index:
                ans = index + 1
                break
        
        return ans