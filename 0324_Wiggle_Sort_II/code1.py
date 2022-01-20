class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        nums.sort()
        nums[0::2], nums[1::2] = reversed(nums[:(len(nums) + 1) // 2:]), reversed(nums[(len(nums) + 1) // 2:])
