class Solution:
    def nextPermutation(self, nums: List[int]) -> None:  
        i = len(nums) - 1
        while i > 0:
            if(nums[i] > nums[i - 1]):
                break  
            i -= 1
        if(i == 0):
            nums.reverse()
        else:
            j = i + 1
            while j < len(nums) and nums[i - 1] < nums[j]:
                j += 1
            j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            nums[i:] = reversed(nums[i:])