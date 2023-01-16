class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        nums = sorted([(num, i) for i, num in enumerate(nums)])

        for length, (numj, j) in enumerate(nums):
            idx = bisect.bisect_left(nums, (target - numj, -float("inf")), 0, length)
            numi, i = nums[idx] if idx < n else [float("inf"), float("inf")]
            if idx < length and numi + numj == target:
                return [i, j]
            
        return []