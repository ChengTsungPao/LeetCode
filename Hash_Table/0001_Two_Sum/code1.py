class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = {}
        for i, num in enumerate(nums):
            if target - num in index:
                return [index[target - num], i]
            index[num] = i
            
        return []