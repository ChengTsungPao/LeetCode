class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for n in nums:
            if(n != 0):
                nums[index] = n
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0
