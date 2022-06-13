class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = reversed(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])