class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n // 2] if n % 2 else (nums[n // 2 - 1] + nums[n // 2]) / 2
        return min(sum([abs(num - math.ceil(median)) for num in nums]), sum([abs(num - math.floor(median)) for num in nums]))