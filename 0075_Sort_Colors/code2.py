class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        i, j = 0, len(nums) - 1
        k = 0
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k = max(i, k)  # 避免i超過k造成已經排好的0換到錯誤的位置
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                k += 0         # 若交換後是0或2，k不可以前進
            else:
                k += 1         # 若遇到1略過