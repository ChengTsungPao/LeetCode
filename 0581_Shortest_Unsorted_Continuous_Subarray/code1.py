class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        sorted_nums = sorted(nums)
        
        i = 0
        while i < n and nums[i] == sorted_nums[i]:
            i += 1
        
        j = n - 1
        while j >= 0 and nums[j] == sorted_nums[j]:
            j -= 1        

        return j - i + 1 if i <= j else 0