class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        n = len(nums)
        
        i = 0
        j = n - 1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1