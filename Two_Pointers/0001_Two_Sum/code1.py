class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        i, j = 0, n - 1
        while i < j:
            numsi, indexi = nums[i]
            numsj, indexj = nums[j]
            
            if numsi + numsj < target:
                i += 1
            elif numsi + numsj > target:
                j -= 1
            else:
                return [indexi, indexj]
            
        return []