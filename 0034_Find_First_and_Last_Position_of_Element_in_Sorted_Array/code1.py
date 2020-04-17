class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = bisect.bisect_left(nums, target)
        if(nums == [] or nums[index - (len(nums) == index)] != target): 
            return [-1,- 1]
        else:        
            return [index, bisect.bisect_right(nums, target) - 1]