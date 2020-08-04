class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:k%len(nums)], nums[k%len(nums):] = nums[len(nums)-k%len(nums):], nums[:len(nums)-k%len(nums)]