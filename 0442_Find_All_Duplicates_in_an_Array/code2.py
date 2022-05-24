class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        index = 0
        while index < n:
            num = nums[index]
            if num <= 0:
                index += 1
                continue

            if nums[num - 1] <= 0:
                nums[num - 1] -= 1
                nums[index] = 0
                index += 1
            else:
                nums[index], nums[num - 1] = nums[num - 1], nums[index]
                nums[num - 1] = -1

        return [i + 1 for i in range(n) if nums[i] <= -2]