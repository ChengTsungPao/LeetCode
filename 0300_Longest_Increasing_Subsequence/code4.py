class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        array_sorted = []
        
        for i in range(len(nums)):
            
            index = bisect.bisect_left(array_sorted, nums[i])
            
            if index >= len(array_sorted):
                array_sorted.append(nums[i])
            else:
                array_sorted[index] = nums[i]
            
        return len(array_sorted)